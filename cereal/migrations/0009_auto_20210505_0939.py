# Generated by Django 3.2 on 2021-05-05 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0008_productcategory_producttags'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='pid',
            field=models.ManyToManyField(to='cereal.ProductModel'),
        ),
        migrations.DeleteModel(
            name='ProductTags',
        ),
    ]
