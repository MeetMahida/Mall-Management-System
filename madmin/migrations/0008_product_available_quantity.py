# Generated by Django 3.0.5 on 2020-05-26 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0007_product_product_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Available_quantity',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
    ]
