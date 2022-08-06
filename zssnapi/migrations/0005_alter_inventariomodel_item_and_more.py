# Generated by Django 4.0.7 on 2022-08-06 04:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zssnapi', '0004_remove_sobreviventemodel_createat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventariomodel',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='zssnapi.itemmodel'),
        ),
        migrations.AlterField(
            model_name='inventariomodel',
            name='sobrevivente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sobrevivente', to='zssnapi.sobreviventemodel'),
        ),
    ]
