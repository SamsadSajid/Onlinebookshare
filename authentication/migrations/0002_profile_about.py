# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-30 19:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
