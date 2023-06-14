from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import redirect, render

from .decorators import unauthenticated_user
from .forms import CreateUserArtistForm, ArtistForm, MusicForm
from .models import UserArtist, Artist, Music


# Create your views here.

@unauthenticated_user
def login_page(request):
    page = 'login'
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, "Incorrect Email Password")
            return redirect('login')
    context = {"page": page}
    return render(request, "login.html", context=context)


def logout_page(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def registration_page(request):
    form = CreateUserArtistForm()
    if request.method == "POST":
        form = CreateUserArtistForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f"Account Created for {first_name} {last_name}")
            return redirect('login')
    context = {
        "form": form
    }
    return render(request, 'registration.html', context=context)


# @unauthenticated_user
@login_required(login_url='login')
def dashboard(request):
    users = UserArtist.objects.all()

    context = {
        'users': users,
    }
    return render(request, 'dashboard.html', context=context)


@login_required(login_url='login')
def all_artists(request):
    artists = Artist.objects.all()
    total_albums = Music.objects.values('album').annotate(total=Count('album')).count()  # Count Total Albums
    context = {
        'artists': artists,
        'total_albums': total_albums
    }
    return render(request, 'artists.html', context)


@login_required(login_url='login')
def create_artist(request):
    form = ArtistForm()
    if request.method == "POST":
        form = ArtistForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artists')
    context = {
        'form': form
    }
    return render(request, 'create_artist.html', context=context)


@login_required(login_url='login')
def update_artist(request, pk):
    artist = Artist.objects.get(id=pk)
    form = ArtistForm(instance=artist)
    if request.method == 'POST':
        form = ArtistForm(request.POST, instance=artist)
        if form.is_valid():
            form.save()
            return redirect('artists')
    context = {
        'form': form
    }
    return render(request, 'update_artist.html', context=context)


@login_required(login_url='login')
def delete_artist(request, pk):
    artist = Artist.objects.get(id=pk)
    if request.method == 'POST':
        artist.delete()
        return redirect('artists')
    context = {
        'artist': artist
    }
    return render(request, 'delete_artist.html', context=context)


@login_required(login_url='login')
def all_music(request):
    musics = Music.objects.all()
    context = {
        'musics': musics
    }
    return render(request, 'music.html', context=context)


@login_required(login_url='login')
def artist_music(request, pk):
    """Music According To Particular Artist"""
    artist = Artist.objects.get(id=pk)
    musics = Music.objects.filter(artist_id=artist)
    context = {
        'artist': artist,
        'musics': musics
    }
    return render(request, 'artist_music.html', context=context)


@login_required(login_url='login')
def create_music(request):
    form = MusicForm()
    if request.method == 'POST':
        form = MusicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('artists')
    context = {
        'form': form
    }
    return render(request, 'create_music.html', context=context)


@login_required(login_url='login')
def update_music(request, pk):
    music = Music.objects.get(id=pk)
    form = MusicForm(instance=music)
    if request.method == 'POST':
        form = MusicForm(request.POST, instance=music)
        if form.is_valid():
            form.save()
            return redirect('music')
    context = {
        'form': form
    }
    return render(request, 'update_music.html', context=context)


@login_required(login_url='login')
def delete_music(request, pk):
    music = Music.objects.get(id=pk)
    if request.method == 'POST':
        music.delete()
        return redirect('music')
    return render(request, 'delete_music.html')
