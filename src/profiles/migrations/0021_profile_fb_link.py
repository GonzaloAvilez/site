# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-21 22:05
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0020_auto_20160922_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fb_link',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
