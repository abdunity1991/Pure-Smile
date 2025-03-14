# Generated by Django 4.2.19 on 2025-02-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='old_cart',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address1',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avaleble',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
