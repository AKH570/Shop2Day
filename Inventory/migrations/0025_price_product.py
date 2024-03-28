# Generated by Django 5.0 on 2024-03-16 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0024_rename_company_brand_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.products'),
        ),
    ]
