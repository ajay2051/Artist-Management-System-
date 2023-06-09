# Generated by Django 4.2.1 on 2023-06-07 05:46

import enumfields.fields
from django.db import migrations

import artist.enums


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_alter_artist_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='gender',
            field=enumfields.fields.EnumField(default='Male', enum=artist.enums.GenderChoice, max_length=10),
        ),
    ]
