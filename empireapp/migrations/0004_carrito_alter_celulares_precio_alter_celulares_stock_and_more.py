# Generated by Django 5.0.6 on 2024-06-15 23:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0003_remove_celulares_estado_remove_laptops_estado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='celulares',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='celulares',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(10000000), django.core.validators.MaxValueValidator(99999999)]),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='precio',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='laptops',
            name='stock',
            field=models.PositiveIntegerField(),
        ),
    ]
