# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 06:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20171002_0958'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_group',
        ),
    ]
