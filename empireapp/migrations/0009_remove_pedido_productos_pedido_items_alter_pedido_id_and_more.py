# Generated by Django 5.0.6 on 2024-06-29 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0008_remove_pedido_items_pedido_productos_alter_pedido_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='productos',
        ),
        migrations.AddField(
            model_name='pedido',
            name='items',
            field=models.ManyToManyField(to='empireapp.cartitem'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]