# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_auto_20171001_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='exam_group',
        ),
        migrations.AddField(
            model_name='group',
            name='group_exam',
            field=models.ManyToManyField(to='students.Exam', verbose_name='Іспит'),
        ),
    ]
