# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-20 03:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kaggle', '0003_auto_20190414_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stdanswer',
            name='comquestion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaggle.ComQuestion'),
        ),
    ]