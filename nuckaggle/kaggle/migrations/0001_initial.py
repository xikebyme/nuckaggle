# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-14 11:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('process_handle', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, verbose_name='题目标题')),
                ('content', models.TextField(max_length=1500, verbose_name='题目内容')),
            ],
            options={
                'verbose_name_plural': '竞赛题目',
            },
        ),
        migrations.CreateModel(
            name='ScoreComq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_score', models.FloatField(default=0, verbose_name='最高分数')),
                ('last_score', models.FloatField(default=0, verbose_name='最新分数')),
                ('ma_sc_dat', models.DateField(default=django.utils.timezone.now, verbose_name='最高分日期')),
                ('comquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaggle.ComQuestion')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process_handle.Schedule')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Team')),
            ],
            options={
                'verbose_name_plural': '对应一个赛程中的一个题目的某个队伍的最高分',
            },
        ),
        migrations.CreateModel(
            name='SourceFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sourcefile', models.FileField(default='source/default.png', upload_to='source/')),
                ('file_called_name', models.CharField(max_length=30, verbose_name='页面显示文件名(文件名+扩展名)')),
                ('comquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaggle.ComQuestion')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process_handle.Schedule')),
            ],
            options={
                'verbose_name_plural': '某赛程赛题对应源文件',
            },
        ),
        migrations.CreateModel(
            name='StdAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdanswer', models.FileField(default='stdAnswer/default.png', upload_to='stdAnswer/')),
                ('comquestion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='kaggle.ComQuestion')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process_handle.Schedule')),
            ],
            options={
                'verbose_name_plural': '某赛程赛题用于核验分数的正确答案',
            },
        ),
        migrations.CreateModel(
            name='SubmitFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitfile', models.FileField(default='submit/default.png', upload_to='submit/%Y/%m/%d')),
                ('score', models.FloatField(default=0, verbose_name='文件得分')),
                ('submit_time', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False, verbose_name='系统计算过得分')),
                ('message', models.CharField(default='系统暂未读取', max_length=30, verbose_name='队伍提交文件的反馈信息')),
                ('comquestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kaggle.ComQuestion')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='process_handle.Schedule')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Team')),
            ],
            options={
                'verbose_name_plural': '某赛程队伍提交的文件',
            },
        ),
    ]
