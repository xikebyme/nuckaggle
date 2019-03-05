# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-05 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kaggle', '0006_auto_20190224_1650'),
    ]

    operations = [
        migrations.CreateModel(
            name='StdAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdanswer', models.FileField(default='stdAnswer/default.png', upload_to='stdAnswer/')),
                ('comquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaggle.ComQuestion')),
            ],
            options={
                'verbose_name_plural': '赛题用于核验分数的正确答案',
            },
        ),
    ]