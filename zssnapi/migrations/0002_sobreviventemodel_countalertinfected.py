# Generated by Django 4.0.7 on 2022-08-04 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zssnapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sobreviventemodel',
            name='countAlertInfected',
            field=models.IntegerField(default=0),
        ),
    ]
