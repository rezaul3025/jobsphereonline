# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-25 12:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobsphereonline', '0005_auto_20161225_1159'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('website', models.CharField(max_length=255)),
                ('logo', models.FileField(upload_to='')),
            ],
        ),
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