from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

from .enums import GenderChoice, Genre


# Create your models here.

class UserArtist(AbstractUser):
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(
        max_length=7,
        choices=[(tag, tag.value) for tag in GenderChoice]  # Choices is a list of Tuple
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Artist(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateTimeField()
    gender = models.CharField(
        max_length=7,
        choices=[(tag, tag.value) for tag in GenderChoice]
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    first_release_year = models.CharField(max_length=255, null=True, blank=True)
    no_of_albums_released = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())


class Music(models.Model):
    artist_id = models.ForeignKey(Artist, related_name='music', on_delete=models.SET_NULL)
    title = models.CharField(max_length=255, null=True, blank=True)
    album = models.CharField(max_length=255, null=True, blank=True)
    genre = models.CharField(
        max_length=7,
        choices=[(tag, tag.value) for tag in Genre]
    )
    created_at = models.DateTimeField(default=timezone.now())
    updated_at = models.DateTimeField(default=timezone.now())
