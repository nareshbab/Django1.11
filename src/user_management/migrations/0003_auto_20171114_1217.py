# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 12:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_auto_20171114_1209'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id',
            new_name='userid',
        ),
    ]
