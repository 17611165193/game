# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2018-05-29 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('combat_team', '0009_merge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combatteam',
            name='introduce',
        ),
        migrations.AddField(
            model_name='teamrequest',
            name='status',
            field=models.SmallIntegerField(choices=[(0, '\u6709\u6548'), (1, '\u5931\u6548')], default=0, verbose_name='\u4fe1\u606f\u72b6\u6001'),
        ),
        migrations.AlterField(
            model_name='teamrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='\u7533\u8bf7\u65f6\u95f4'),
        ),
    ]
