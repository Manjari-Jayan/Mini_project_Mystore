# Generated by Django 4.2.5 on 2023-10-20 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0019_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='back_camera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='front_camera',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='processor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='ram',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='rom',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]