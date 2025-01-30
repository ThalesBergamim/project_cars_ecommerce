# Generated by Django 5.1.4 on 2025-01-27 23:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0004_carinventory'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Marca', 'verbose_name_plural': 'Marcas'},
        ),
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Carro', 'verbose_name_plural': 'Carros'},
        ),
        migrations.AlterModelOptions(
            name='carinventory',
            options={'ordering': ['-created_at'], 'verbose_name': 'Inventário', 'verbose_name_plural': 'Inventários'},
        ),
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(error_messages={'unique': 'Esta marca já está cadastrada no sistema.'}, max_length=200, unique=True, verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='car_brand', to='ecom.brand', verbose_name='Marca'),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='car',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='cars/', verbose_name='Imagem'),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=200, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='car',
            name='plate',
            field=models.CharField(max_length=10, verbose_name='Placa'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_fabrication',
            field=models.IntegerField(verbose_name='Ano de Fabricação'),
        ),
        migrations.AlterField(
            model_name='car',
            name='year_model',
            field=models.IntegerField(verbose_name='Ano do Modelo'),
        ),
        migrations.AlterField(
            model_name='carinventory',
            name='cars_count',
            field=models.IntegerField(verbose_name='Quantidade de Carros'),
        ),
        migrations.AlterField(
            model_name='carinventory',
            name='cars_value',
            field=models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor Total'),
        ),
        migrations.AlterField(
            model_name='carinventory',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação'),
        ),
    ]
