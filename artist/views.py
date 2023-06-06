from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .decorators import unauthenticated_user
from .forms import CreateUserForm


# Create your views here.

@unauthenticated_user
def login_page(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('')
        else:
            messages.info(request, "Incorrect Username Password")
            return redirect('login')
    context = {}
    return render(request, "login.html", context=context)


def logout_page(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def registration_page(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account Created for" + username)
            return redirect('login')
    context = {
        "form": form
    }
    return render(request, 'registration.html', context=context)


@unauthenticated_user
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard.html')
