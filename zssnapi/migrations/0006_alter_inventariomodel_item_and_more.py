# Generated by Django 4.0.7 on 2022-08-06 04:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zssnapi', '0005_alter_inventariomodel_item_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventariomodel',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='zssnapi.itemmodel'),
        ),
        migrations.AlterField(
            model_name='inventariomodel',
            name='sobrevivente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventario', to='zssnapi.sobreviventemodel'),
        ),
    ]
