# Generated by Django 5.0 on 2024-05-26 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_ordereditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordereditem',
            name='orderedSuccess',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='ordereditem',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
