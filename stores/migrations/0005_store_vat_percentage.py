# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-10 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stores', '0004_auto_20161217_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='vat_percentage',
            field=models.PositiveIntegerField(default=0),
        ),
    ]