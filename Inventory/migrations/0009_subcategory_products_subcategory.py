# Generated by Django 5.0 on 2024-02-18 15:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
        ('Inventory', '0008_rename_name_brand_supplier_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SUBCATEGORY',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('icon', models.ImageField(null=True, upload_to='Subcategory')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Category.category')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='subcategory',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.subcategory'),
        ),
    ]
