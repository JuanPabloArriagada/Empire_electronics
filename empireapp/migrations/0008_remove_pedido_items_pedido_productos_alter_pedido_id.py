# Generated by Django 5.0.6 on 2024-06-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0007_remove_pedido_items_alter_pedido_total_pedido_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='items',
        ),
        migrations.AddField(
            model_name='pedido',
            name='productos',
            field=models.ManyToManyField(to='empireapp.producto'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]