# Generated by Django 4.2.5 on 2023-09-27 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0011_product_series'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='series',
        ),
    ]