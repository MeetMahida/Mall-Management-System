# Generated by Django 3.0.5 on 2020-05-24 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('madmin', '0004_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='p_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='supplierName',
            field=models.CharField(max_length=100),
        ),
    ]
