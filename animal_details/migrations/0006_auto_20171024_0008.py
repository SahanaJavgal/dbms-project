# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 18:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_details', '0005_auto_20171023_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]