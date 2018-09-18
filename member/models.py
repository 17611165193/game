# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(verbose_name=u'用户名称', max_length=50)
    password = models.CharField(verbose_name=u'用户密码', max_length=50)
    mailbox = models.EmailField(verbose_name='邮箱', max_length=20, null=True)
    phone_number = models.CharField(verbose_name=u"联系电话", max_length=11, null=True)
    qq = models.CharField(verbose_name=u"qq", max_length=15, null=True)
    weixin = models.CharField(verbose_name=u"微信", max_length=15, null=True)
    introduce = models.TextField(null=True)
    created_at = models.DateTimeField(verbose_name=u"创建时间", auto_created=True, null=True)

    def __unicode__(self):
        return self.username


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    team_people = models.CharField(max_length=100)
    team_introduce = models.CharField(max_length=200)

    def __str__(self):
        return self.team_name
