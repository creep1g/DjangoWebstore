# Generated by Django 3.2 on 2021-05-04 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210504_1539'),
        ('cereal', '0001_initial'),
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
            ],
        ),
        migrations.RemoveField(
            model_name='customermodel',
            name='cid',
        ),
        migrations.RemoveField(
            model_name='customermodel',
            name='zipcode',
        ),
        migrations.DeleteModel(
            name='ProfilePictureModel',
        ),
        migrations.RemoveField(
            model_name='productmodel',
            name='id',
        ),
        migrations.AddField(
            model_name='productimagemodel',
            name='default',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='productimagemodel',
            name='image',
            field=models.ImageField(default='', upload_to='images/products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productimagemodel',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='productimagemodel',
            name='pid',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.DO_NOTHING, to='cereal.productmodel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='description',
            field=models.CharField(default='', max_length=2500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='pid',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productmodel',
            name='rating',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ordermodel',
            name='CID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.profile'),
        ),
        migrations.AlterField(
            model_name='shoppingcartmodel',
            name='CID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.profile'),
        ),
        migrations.DeleteModel(
            name='AccountModel',
        ),
        migrations.DeleteModel(
            name='CustomerModel',
        ),
        migrations.DeleteModel(
            name='LocationsModel',
        ),
        migrations.AddField(
            model_name='producttags',
            name='pid',
            field=models.ManyToManyField(to='cereal.ProductModel'),
        ),
    ]