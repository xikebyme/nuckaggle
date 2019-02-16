# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-02-16 14:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_confirm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='confirm',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
