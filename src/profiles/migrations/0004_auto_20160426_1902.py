# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-27 00:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20160426_1856'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='short_name',
            new_name='market',
        ),
        migrations.AddField(
            model_name='profile',
            name='bio2',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Nuestra historia'),
        ),
    ]
