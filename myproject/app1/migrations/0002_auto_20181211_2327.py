# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-12-11 23:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='customers',
        ),
    ]
