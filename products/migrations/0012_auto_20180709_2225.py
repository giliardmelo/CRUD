# Generated by Django 2.0.7 on 2018-07-10 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20180709_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CPF',
            field=models.CharField(max_length=11),
        ),
    ]
