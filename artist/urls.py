from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('registration/', views.registration_page, name='registration'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('artists/', views.all_artists, name='artists'),
    path('create-artist/', views.create_artist, name='create-artist'),
    path('update-artist/<int:pk>/', views.update_artist, name='update-artist'),
    path('delete-artist/<int:pk>/', views.delete_artist, name='delete-artist'),


    path('music/', views.all_music, name='music'),
    path('artist-music/<int:pk>/', views.artist_music, name='artist-music'),
    path('create-music/', views.create_music, name='create-music'),
    path('update-music/<int:pk>/', views.update_music, name='update-music'),
    path('delete-music/<int:pk>/', views.delete_music, name='delete-music')
]
