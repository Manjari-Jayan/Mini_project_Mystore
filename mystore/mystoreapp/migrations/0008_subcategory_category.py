# Generated by Django 4.2.5 on 2023-09-25 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystoreapp', '0007_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mystoreapp.category'),
            preserve_default=False,
        ),
    ]
