# Generated by Django 3.2 on 2021-05-11 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0020_auto_20210511_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='searches',
            name='token',
            field=models.CharField(default=0, max_length=99999),
            preserve_default=False,
        ),
    ]
