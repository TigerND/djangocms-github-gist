# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-04 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_githubgist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gistpluginmodel',
            name='name',
            field=models.CharField(blank=True, help_text='Name (optional)', max_length=32, null=True, verbose_name=b'Name'),
        ),
    ]
