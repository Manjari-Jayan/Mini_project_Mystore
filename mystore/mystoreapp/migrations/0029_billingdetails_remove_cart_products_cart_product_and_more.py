# Generated by Django 4.2.5 on 2024-01-23 06:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mystoreapp', '0028_rename_product_cart_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('street_address', models.CharField(max_length=255)),
                ('apartment_suite_unit', models.CharField(blank=True, max_length=255, null=True)),
                ('town_city', models.CharField(max_length=255)),
                ('postcode_zip', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='cart',
            name='products',
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.TextField(blank=True, default={'objects': []}, null=True),
        ),
        migrations.DeleteModel(
            name='DeliveryAgent',
        ),
    ]
