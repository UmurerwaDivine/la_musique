# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-21 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('own', '0007_auto_20190418_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, default=''),
        ),
    ]
