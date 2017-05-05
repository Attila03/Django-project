# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-05-05 11:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0015_cart_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ordersite.Customer'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
