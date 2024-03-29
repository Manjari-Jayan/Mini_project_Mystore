# Generated by Django 4.2.5 on 2024-01-22 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0022_rename_date_added_cart_created_remove_cart_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='order_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='cart',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cart',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.JSONField(blank=True, default={'objects': []}, null=True),
        ),
    ]
