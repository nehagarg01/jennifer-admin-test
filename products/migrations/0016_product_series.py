# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-24 23:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
        ('products', '0015_auto_20161022_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='series',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='series.Series'),
        ),
    ]
