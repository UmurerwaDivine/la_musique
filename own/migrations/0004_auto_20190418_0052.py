# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 00:52
from __future__ import unicode_literals

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('own', '0003_auto_20190417_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='lyrics',
            field=tinymce.models.HTMLField(),
        ),
    ]
