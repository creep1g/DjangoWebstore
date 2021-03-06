# Generated by Django 3.2 on 2021-05-05 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210504_1548'),
        ('cereal', '0013_merge_0002_candycategory_0012_auto_20210505_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShoppingCartModel',
            fields=[
                ('scid', models.AutoField(primary_key=True, serialize=False)),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user.profile')),
                ('pid', models.ManyToManyField(to='cereal.ProductModel')),
            ],
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='category',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productimagemodel',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productimagemodel',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cereal.productmodel'),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='SCID',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='cereal.shoppingcartmodel'),
            preserve_default=False,
        ),
    ]
