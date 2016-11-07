# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-07 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpage',
            name='page_number',
            field=models.PositiveSmallIntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
