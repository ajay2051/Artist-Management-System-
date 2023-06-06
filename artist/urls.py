from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_page, name='login'),
    path('logout', views.logout_page, name='logout'),
    path('registration', views.registration_page, name='registration'),

    path('dashboard', views.dashboard, name='dashboard')
]
