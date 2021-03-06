# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-28 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=100)),
                ('team_people', models.CharField(max_length=100)),
                ('team_introduce', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='\u7528\u6237\u540d\u79f0')),
                ('password', models.CharField(max_length=50, verbose_name='\u7528\u6237\u5bc6\u7801')),
                ('mailbox', models.EmailField(max_length=20, null=True, verbose_name='\u90ae\u7bb1')),
                ('phone_number', models.CharField(max_length=11, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('qq', models.CharField(max_length=15, null=True, verbose_name='qq')),
                ('weixin', models.CharField(max_length=15, null=True, verbose_name='\u5fae\u4fe1')),
                ('introduce', models.TextField(null=True)),
            ],
        ),
    ]
