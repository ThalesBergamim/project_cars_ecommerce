# Generated by Django 5.1.4 on 2025-01-28 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0005_alter_brand_options_alter_car_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Cor'),
        ),
        migrations.AddField(
            model_name='car',
            name='potency',
            field=models.IntegerField(blank=True, null=True, verbose_name='Potência (CV)'),
        ),
    ]
