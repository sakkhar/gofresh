# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-10 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0005_store_vat_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='vat_percentage',
            field=models.FloatField(default=0),
        ),
    ]