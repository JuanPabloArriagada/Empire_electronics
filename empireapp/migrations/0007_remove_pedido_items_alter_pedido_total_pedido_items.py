# Generated by Django 5.0.6 on 2024-06-29 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empireapp', '0006_alter_pedido_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='items',
        ),
        migrations.AlterField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
        migrations.AddField(
            model_name='pedido',
            name='items',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
