# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-15 17:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170915_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 15, 17, 1, 45, 829602, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 9, 15, 17, 1, 45, 828704, tzinfo=utc)),
        ),
    ]
