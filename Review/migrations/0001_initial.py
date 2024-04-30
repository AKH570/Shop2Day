# Generated by Django 5.0 on 2024-04-25 02:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Inventory', '0003_rename_valuename_attributevalue_color_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True, max_length=200, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('ip', models.CharField(blank=True, max_length=100)),
                ('status', models.BooleanField(default=True)),
                ('commentDate', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(db_column='author', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(db_column='product', null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventory.products')),
            ],
            options={
                'verbose_name_plural': 'REVIEWS',
            },
        ),
    ]
