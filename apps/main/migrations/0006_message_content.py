# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-08-25 00:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20190824_2323'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(null=True),
        ),
    ]
