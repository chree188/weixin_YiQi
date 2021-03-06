# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-08 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20180708_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='UserProFilebg/avatar/%y/%d/bd3b8058503c4d99ab24456be2308859'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='background',
            field=models.ImageField(blank=True, default='/default/default.jpg', null=True, upload_to='UserProFilebg/%Y/%m/bd3b8058503c4d99ab24456be2308859', verbose_name='背景图'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_bh',
            field=models.CharField(default='581f6e37e6104c3fb3a5e418094b07d2', max_length=50, unique=True, verbose_name='用户唯一ID'),
        ),
    ]
