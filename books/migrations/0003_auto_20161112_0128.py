# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-12 01:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_bookpage_page_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookpage',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
