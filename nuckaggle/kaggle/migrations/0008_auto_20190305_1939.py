# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-03-05 11:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kaggle', '0007_stdanswer'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitfile',
            name='message',
            field=models.CharField(default='系统暂未读取', max_length=30, verbose_name='队伍提交文件的反馈信息'),
        ),
        migrations.AlterField(
            model_name='submitfile',
            name='score',
            field=models.FloatField(default=0, verbose_name='文件得分'),
        ),
    ]