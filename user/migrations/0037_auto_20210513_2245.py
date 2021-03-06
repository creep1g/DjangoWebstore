# Generated by Django 3.2 on 2021-05-13 22:45

from django.db import migrations, models
import django.db.models.deletion
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0036_merge_0031_alter_profile_zipcode_0035_profile_zipcode'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='locationsmodel',
            options={'ordering': ['country']},
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_cvc',
            field=models.IntegerField(null=True, validators=[user.models.CVCValidator()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_expiration',
            field=models.DateField(max_length=8, null=True, validators=[user.models.validate_date]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_holder',
            field=models.CharField(max_length=36, null=True, validators=[user.models.NameValidator()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='card_number',
            field=models.CharField(max_length=19, null=True, validators=[user.models.CCValidator()]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=255, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location_id',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to='user.locationsmodel', verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(null=True, upload_to='users/'),
        ),
    ]
