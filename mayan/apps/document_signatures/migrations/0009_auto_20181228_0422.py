# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-28 04:22
from __future__ import unicode_literals

from django.db import migrations, models
import mayan.apps.document_signatures.models
import mayan.apps.document_signatures.storages


class Migration(migrations.Migration):

    dependencies = [
        ('document_signatures', '0008_auto_20180429_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detachedsignature',
            name='signature_file',
            field=models.FileField(blank=True, null=True, storage=mayan.apps.document_signatures.storages.storage_detachedsignature_wrapper, upload_to=mayan.apps.document_signatures.models.upload_to, verbose_name='Signature file'),
        ),
    ]
