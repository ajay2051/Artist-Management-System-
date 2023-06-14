# Generated by Django 4.2.1 on 2023-06-12 06:19

import enumfields.fields
from django.db import migrations

import artist.enums


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0005_alter_userartist_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='genre',
            field=enumfields.fields.EnumField(default='Rnb', enum=artist.enums.Genre, max_length=10),
        ),
    ]
