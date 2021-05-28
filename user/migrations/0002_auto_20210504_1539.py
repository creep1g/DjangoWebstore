# Generated by Django 3.2 on 2021-05-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocationsModel',
            fields=[
                ('zipcode', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
            ],
            options={
                'ordering': ['-country', '-zipcode'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='house_number',
            field=models.CharField(default='', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='street_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(upload_to='static/images/users'),
        ),
        migrations.AddField(
            model_name='profile',
            name='zipcode',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='user.locationsmodel'),
            preserve_default=False,
        ),
    ]