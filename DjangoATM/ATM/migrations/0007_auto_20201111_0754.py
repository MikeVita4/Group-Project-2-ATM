# Generated by Django 3.1.3 on 2020-11-11 12:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATM', '0006_auto_20201111_0730'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='account_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='card',
            name='exp_date',
            field=models.DateField(default=datetime.datetime(2023, 11, 11, 7, 54, 9, 517406)),
        ),
    ]
