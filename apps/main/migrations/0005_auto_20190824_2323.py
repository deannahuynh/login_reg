# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-24 23:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190824_2321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=80),
        ),
    ]
