# Generated by Django 4.2.19 on 2025-02-15 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='pr',
        ),
    ]
