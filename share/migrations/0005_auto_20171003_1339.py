# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-03 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0004_auto_20171003_1328'),
    ]

    operations = [
        migrations.RenameField(
            model_name='key',
            old_name='username',
            new_name='shared_to',
        ),
        migrations.RenameField(
            model_name='key',
            old_name='space_shared',
            new_name='space_allotted',
        ),
    ]
