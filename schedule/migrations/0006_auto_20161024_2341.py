# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0005_auto_20161023_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='task_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='schedule',
            name='task_total',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='status',
            field=models.CharField(choices=[('p', 'pending'), ('i', 'in progress'), ('e', 'error'), ('c', 'completed')], default='p', max_length=2),
        ),
    ]
