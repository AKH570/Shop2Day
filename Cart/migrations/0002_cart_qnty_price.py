# Generated by Django 5.0 on 2024-05-10 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='qnty_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]