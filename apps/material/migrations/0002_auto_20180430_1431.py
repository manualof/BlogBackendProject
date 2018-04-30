# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-04-30 06:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='postbaseinfo',
            name='is_commentable',
            field=models.BooleanField(default=True, help_text='是否可评论', verbose_name='是否可评论'),
        ),
        migrations.AlterField(
            model_name='materialtag',
            name='color',
            field=models.CharField(default='blue', help_text='颜色', max_length=20, verbose_name='颜色'),
        ),
        migrations.AlterField(
            model_name='postbaseinfo',
            name='front_image',
            field=models.ImageField(blank=True, help_text='大图833*217，小图243*207', null=True, upload_to='material/post/image/%y/%m', verbose_name='封面图'),
        ),
    ]
