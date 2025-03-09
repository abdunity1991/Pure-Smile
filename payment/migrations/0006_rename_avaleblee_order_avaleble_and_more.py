# Generated by Django 4.2.19 on 2025-02-25 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_alter_shippingaddress_shipping_address1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='avaleblee',
            new_name='avaleble',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='fullname',
            new_name='fullnam',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='phonee',
            new_name='phone',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address1e',
        ),
        migrations.AddField(
            model_name='order',
            name='address1',
            field=models.TextField(default=1, max_length=15000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shipping_address2',
            field=models.TextField(blank=True, max_length=15000, null=True),
        ),
    ]
