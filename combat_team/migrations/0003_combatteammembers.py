# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 06:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
        ('combat_team', '0002_auto_20180428_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='CombatTeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('combat_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='combat_team.CombatTeam', verbose_name='\u6218\u961f')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='member.User', verbose_name='\u6218\u961f\u4eba\u5458')),
            ],
        ),
    ]