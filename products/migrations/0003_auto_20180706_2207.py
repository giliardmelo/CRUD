# Generated by Django 2.0.7 on 2018-07-07 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20180706_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='CPF',
            field=models.IntegerField(blank=True, max_length=11),
        ),
    ]
