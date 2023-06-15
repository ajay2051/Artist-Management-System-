from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from enumfields import EnumField

from .enums import GenderChoice, Genre

# Create your models here.

class UserArtist(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = EnumField(
        GenderChoice, max_length=10, default=GenderChoice.Male
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Artist(models.Model):
    objects = None
    name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    gender = EnumField(
        GenderChoice, max_length=10, default=GenderChoice.Male
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    first_release_year = models.CharField(max_length=255, null=True, blank=True)
    no_of_albums_released = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Music(models.Model):
    objects = None
    artist_id = models.ForeignKey(Artist, related_name='music', on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    album = models.CharField(max_length=255, null=True, blank=True)
    genre = EnumField(
        Genre, max_length=10, default=Genre.Rnb
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
