# Generated by Django 3.2 on 2021-05-12 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0022_auto_20210511_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='zipcode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.locationsmodel'),
        ),
    ]