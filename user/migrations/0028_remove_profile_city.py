# Generated by Django 3.2 on 2021-05-12 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0027_profile_location_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city',
        ),
    ]
