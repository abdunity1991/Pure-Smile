# Generated by Django 4.2.19 on 2025-02-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_address1_shippingaddress_shipping_address1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_address1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_address2',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
