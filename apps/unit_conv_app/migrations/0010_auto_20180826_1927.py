# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-26 19:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unit_conv_app', '0009_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='upload_file',
            field=models.FileField(default=None, upload_to='upload_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='upload',
            name='uploader',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='uploaded_files', to='unit_conv_app.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='upload',
            name='file_name',
            field=models.CharField(max_length=255),
        ),
    ]
