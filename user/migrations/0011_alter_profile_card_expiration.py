# Generated by Django 3.2 on 2021-05-11 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20210511_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='card_expiration',
            field=models.DateField(max_length=8, null=True),
        ),
    ]