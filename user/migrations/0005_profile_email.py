# Generated by Django 3.2 on 2021-05-05 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210504_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]