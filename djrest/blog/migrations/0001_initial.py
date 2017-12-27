# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-27 07:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', error_messages={'blank': 'this title is blank, please try again!', 'unique': 'this title is not unique, please try again!'}, help_text='must be an unique title', max_length=20, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('content', models.TextField(blank=True, null=True)),
                ('view_count', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Posts',
            },
        ),
    ]