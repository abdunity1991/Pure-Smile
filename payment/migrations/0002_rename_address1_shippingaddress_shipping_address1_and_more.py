# Generated by Django 4.2.19 on 2025-02-25 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address1',
            new_name='shipping_address1',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='address2',
            new_name='shipping_address2',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='avaleble',
            new_name='shipping_avaleble',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='city',
            new_name='shipping_city',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='name',
            new_name='shipping_name',
        ),
        migrations.RenameField(
            model_name='shippingaddress',
            old_name='phone',
            new_name='shipping_phone',
        ),
    ]
