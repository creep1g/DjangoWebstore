# Generated by Django 3.2 on 2021-05-06 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0032_alter_productmodel_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcategory',
            name='pid',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.ManyToManyField(related_name='products', to='cereal.ProductCategory'),
        ),
    ]
