# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-11-08 08:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='pro_pic',
            new_name='profile_pic',
        ),
    ]
