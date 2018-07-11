# Generated by Django 2.0.7 on 2018-07-09 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_product_idade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Nome',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='product',
            name='idade',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='nasc',
            field=models.DateField(null=True),
        ),
    ]
