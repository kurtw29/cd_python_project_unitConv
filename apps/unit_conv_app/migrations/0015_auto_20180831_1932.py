# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-31 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unit_conv_app', '0014_auto_20180831_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='status',
            field=models.CharField(default='', max_length=45),
        ),
    ]
