# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-18 08:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['updated']},
        ),
        migrations.AlterField(
            model_name='book',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
