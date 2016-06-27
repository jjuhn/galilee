# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-25 22:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='email',
        ),
        migrations.RemoveField(
            model_name='signup',
            name='full_name',
        ),
        migrations.AddField(
            model_name='signup',
            name='first_name',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='signup',
            name='last_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]