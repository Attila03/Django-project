# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-03-08 17:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordersite', '0014_auto_20170224_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
