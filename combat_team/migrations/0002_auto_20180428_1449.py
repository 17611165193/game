# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 06:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('combat_team', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='combatteammembers',
            name='combat_team',
        ),
        migrations.RemoveField(
            model_name='combatteammembers',
            name='member',
        ),
        migrations.DeleteModel(
            name='CombatTeamMembers',
        ),
    ]