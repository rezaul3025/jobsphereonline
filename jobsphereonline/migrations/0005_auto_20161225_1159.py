# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-25 11:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsphereonline', '0004_auto_20161225_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.ManyToManyField(to='jobsphereonline.Location'),
        ),
        migrations.AlterField(
            model_name='job',
            name='tag',
            field=models.ManyToManyField(to='jobsphereonline.Tag'),
        ),
    ]
