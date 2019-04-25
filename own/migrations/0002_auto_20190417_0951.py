# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-17 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('own', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artistName', models.CharField(max_length=30)),
                ('artistInfo', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic', models.ImageField(upload_to='images/albumart/')),
                ('songName', models.CharField(max_length=30)),
                ('audio_track', models.FileField(upload_to='songs/')),
                ('lyrics', models.FileField(upload_to='lyrics/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='own.Artist')),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]