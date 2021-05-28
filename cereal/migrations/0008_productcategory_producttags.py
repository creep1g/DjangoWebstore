# Generated by Django 3.2 on 2021-05-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0007_auto_20210505_0924'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('category', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ManyToManyField(to='cereal.ProductCategory')),
                ('pid', models.ManyToManyField(to='cereal.ProductModel')),
            ],
        ),
    ]