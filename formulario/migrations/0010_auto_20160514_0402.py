# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-14 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formulario', '0009_auto_20160514_0342'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registro',
            name='picture',
            field=models.ImageField(blank=True, upload_to=b''),
        ),
    ]
