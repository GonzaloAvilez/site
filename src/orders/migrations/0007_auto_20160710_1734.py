# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-10 22:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20160627_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=20, verbose_name='C\xf3digo postal'),
        ),
    ]
