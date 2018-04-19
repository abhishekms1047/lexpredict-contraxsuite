# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-05 17:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0012_auto_20180401_2046'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='status',
        ),
        migrations.AddField(
            model_name='project',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='project.ProjectStatus'),
        ),
    ]