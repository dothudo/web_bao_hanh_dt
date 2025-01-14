# Generated by Django 5.0.4 on 2024-04-27 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warranty', '0002_alter_product_manufacturer_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='requires_repair',
            field=models.IntegerField(choices=[(0, 'Đang sử dụng'), (1, 'Đang sửa chữa')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='warranty_product',
            field=models.IntegerField(choices=[(0, 'Hết bảo hành'), (1, 'Con bảo hành')]),
        ),
    ]
