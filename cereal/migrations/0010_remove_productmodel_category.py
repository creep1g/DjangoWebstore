# Generated by Django 3.2 on 2021-05-05 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cereal', '0009_auto_20210505_0939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='category',
        ),
    ]
