# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-22 02:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='datetime',
        ),
        migrations.AddField(
            model_name='schedule',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
