# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-18 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('own', '0005_auto_20190418_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='audio_track',
            field=models.FileField(upload_to='songs/'),
        ),
    ]
