# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-23 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0003_auto_20170122_1038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='cost',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='topping',
            name='name',
            field=models.CharField(choices=[('VEG', (('BO', 'Black Olives'), ('PN', 'Paneer'), ('MH', 'Mushroom'), ('CA', 'Capsicum'), ('GC', 'Golden Corn'), ('JP', 'Jalapeno'), ('FT', 'Fresh Tomato'), ('RP', 'Red Pepper'))), ('NON-VEG', (('BC', 'Barbeque Chicken'), ('SC', 'Spicy Chicken'), ('CC', 'Chunky Chicken'), ('CS', 'Chicken Salami'), ('CR', 'Chicken Rashers')))], max_length=50, unique=True),
        ),
    ]
