# Generated by Django 3.0.5 on 2020-06-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0011_auto_20200527_1452'),
        ('billing', '0002_auto_20200610_2229'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='product',
        ),
        migrations.AddField(
            model_name='customer',
            name='product',
            field=models.ManyToManyField(to='madmin.Product'),
        ),
    ]