# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0007_auto_20170822_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='status',
            field=models.TextField(blank=True, default=''),
        ),
    ]
