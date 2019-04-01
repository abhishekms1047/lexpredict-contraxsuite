# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-19 15:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from apps.document.constants import DOCUMENT_TYPE_PK_GENERIC_DOCUMENT


class Migration(migrations.Migration):
    dependencies = [
        ('rawdb', '0014_auto_20190104_1605'),
    ]

    operations = [
        migrations.RunSQL(
            "update rawdb_savedfilter set document_type_id='{0}' where document_type_id is null"
                .format(DOCUMENT_TYPE_PK_GENERIC_DOCUMENT)
        ),
        migrations.AlterField(
            model_name='savedfilter',
            name='document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='document.DocumentType'),
        ),
    ]