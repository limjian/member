# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-11 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_comment_approved_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='approved_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='updated_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]