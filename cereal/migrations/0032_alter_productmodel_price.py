# Generated by Django 3.2 on 2021-05-05 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0031_ordermodel_productcategory_productmodel_shoppingcartmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.FloatField(),
        ),
    ]
