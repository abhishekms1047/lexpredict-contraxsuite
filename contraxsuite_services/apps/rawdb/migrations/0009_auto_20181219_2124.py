# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-12-19 21:24
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
import django.core.serializers.json
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rawdb', '0008_auto_20181219_2122'),
    ]

    operations = [
        migrations.AddField(
            model_name='savedfilter',
            name='columns',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
        migrations.RemoveField(model_name='savedfilter', name='order_by'),
        migrations.AddField(
            model_name='savedfilter',
            name='order_by',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, encoder=django.core.serializers.json.DjangoJSONEncoder, null=True),
        ),
    ]