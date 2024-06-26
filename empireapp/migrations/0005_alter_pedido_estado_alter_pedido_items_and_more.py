# Generated by Django 5.0.6 on 2024-06-28 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0004_alter_cartitem_quantity_alter_laptops_almacenamiento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='estado',
            field=models.CharField(choices=[('sin confirmar', 'SIN CONFIRMAR'), ('en preparacion', 'EN PREPARACION'), ('enviado', 'ENVIADO'), ('entregado', 'ENTREGADO'), ('devuelto', 'DEVUELTO'), ('rechazado', 'RECHAZADO'), ('cancelado', 'CANCELADO')], default='pendiente', max_length=20),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='items',
            field=models.ManyToManyField(to='empireapp.cartitem'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
