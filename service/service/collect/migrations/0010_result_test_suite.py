# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 09:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collect', '0009_auto_20170822_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='test_suite',
            field=models.TextField(blank=True, default='NA'),
        ),
    ]
