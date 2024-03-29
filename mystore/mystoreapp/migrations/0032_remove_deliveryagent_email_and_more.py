# Generated by Django 4.2.5 on 2024-02-01 05:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mystoreapp', '0031_deliveryagent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliveryagent',
            name='email',
        ),
        migrations.RemoveField(
            model_name='deliveryagent',
            name='license_number',
        ),
        migrations.RemoveField(
            model_name='deliveryagent',
            name='name',
        ),
        migrations.RemoveField(
            model_name='deliveryagent',
            name='password',
        ),
        migrations.RemoveField(
            model_name='deliveryagent',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='deliveryagent',
            name='status',
        ),
        migrations.RemoveField(
            model_name='deliveryagent',
            name='username',
        ),
        migrations.RemoveField(
            model_name='deliveryagent',
            name='vechicle_type',
        ),
        migrations.AddField(
            model_name='deliveryagent',
            name='distance',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deliveryagent',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='deliveryagent',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='deliveryagent',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='deliveryagent',
            name='pincode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='deliveryagent',
            name='place',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryagent',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='deliveryagent',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
