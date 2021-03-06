# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-13 02:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171213_0934'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('private', 'Private')], default='draft', max_length=120),
        ),
    ]
