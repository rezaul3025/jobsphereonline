# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-24 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsphereonline', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]