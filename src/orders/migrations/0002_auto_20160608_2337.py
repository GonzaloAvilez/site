# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-06-09 04:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=250, verbose_name='Direcci\xf3n'),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=100, verbose_name='Ciudad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='order',
            name='first_name',
            field=models.CharField(max_length=50, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='order',
            name='last_name',
            field=models.CharField(max_length=50, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='order',
            name='postal_code',
            field=models.CharField(max_length=20, verbose_name='C\xf3digo postal'),
        ),
    ]
