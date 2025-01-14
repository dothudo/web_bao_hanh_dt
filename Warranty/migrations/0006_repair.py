# Generated by Django 5.0.4 on 2024-04-30 08:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warranty', '0005_remove_product_description_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='repair',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fault_status', models.CharField(blank=True, max_length=1000, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Warranty.product')),
            ],
        ),
    ]
