# Generated by Django 5.0 on 2024-02-08 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0005_rename_discount_price_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='tag_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
