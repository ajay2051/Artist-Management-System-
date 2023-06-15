from django.contrib.auth.models import Group
from django.db.models.signals import post_save

from .models import UserArtist


def user_profile(sender, instance, created, **kwargs):
    """This signals is created to automatically add newly registered user to group user"""
    if created:
        group = Group.objects.get(name='user')
        instance.groups.add(group)
        UserArtist.objects.create(user=instance, name=instance.first_name)
        print('User Created')


post_save.connect(user_profile, sender=UserArtist)
