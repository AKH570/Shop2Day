# Generated by Django 5.0 on 2024-02-20 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0012_alter_image_imglink'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='stocks',
            name='stocks_qty',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='attributevalue',
            field=models.ManyToManyField(blank=True, to='Inventory.attributevalue'),
        ),
        migrations.AlterField(
            model_name='stocks',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
    ]
