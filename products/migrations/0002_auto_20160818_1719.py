# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-18 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_type', models.CharField(choices=[('MA', 'Material'), ('ST', 'Style'), ('FT', 'Feature')], max_length=3)),
                ('title', models.CharField(max_length=255)),
                ('handle', models.CharField(help_text='shopify tag', max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='body_html',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AddField(
            model_name='product',
            name='attributes',
            field=models.ManyToManyField(to='products.ProductAttribute'),
        ),
    ]