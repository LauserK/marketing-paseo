# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-20 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='file',
            field=models.FileField(blank=True, default='', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='propaganda',
            name='video',
            field=models.FileField(blank=True, default='', upload_to='videos/'),
        ),
    ]
