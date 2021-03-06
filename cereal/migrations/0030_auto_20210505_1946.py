# Generated by Django 3.2 on 2021-05-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0029_auto_20210505_1838'),
    ]

    operations = [
        migrations.CreateModel(
            name='CandyCategory',
            fields=[('CHAR', models.CharField(max_length=255))]
        ),
        migrations.DeleteModel(
            name='CandyCategory',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='CID',
        ),
        migrations.RemoveField(
            model_name='ordermodel',
            name='SCID',
        ),
        migrations.RemoveField(
            model_name='productcategory',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='shoppingcartmodel',
            name='pid',
        ),
        migrations.RemoveField(
            model_name='shoppingcartmodel',
            name='user',
        ),
        migrations.CreateModel(
            name='CartContentsModel',
            fields= [('char', models.CharField(max_length=200))]
        ),
        migrations.DeleteModel(
            name='CartContentsModel',
        ),
        migrations.DeleteModel(
            name='OrderModel',
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
        migrations.DeleteModel(
            name='ProductModel',
        ),
        migrations.DeleteModel(
            name='ShoppingCartModel',
        ),
    ]
