# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.db import models

# Create your models here.
from member.models import User


class GameType(models.Model):
    name = models.CharField(verbose_name='游戏类型', max_length=20 )
    people_number = models.IntegerField(verbose_name='需要人数')
    created_at = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)


class CombatTeam(models.Model):
    name = models.CharField(verbose_name=u"战队名", max_length=100)
    leader = models.ForeignKey(User, verbose_name=u"战队队长")
    type = models.ForeignKey(GameType, verbose_name=u"游戏类型", null=True)
    phone_number = models.CharField(verbose_name=u"联系电话", max_length=11)
    slogan = models.TextField()
    created_at = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)

    def __str__(self):
        return self.name


class CombatTeamMembers(models.Model):
    combat_team = models.ForeignKey(CombatTeam, verbose_name=u"战队")
    member = models.ForeignKey(User, verbose_name=u"战队人员")
    created_at = models.DateTimeField(verbose_name=u"创建时间", auto_now_add=True)


class TeamRequest(models.Model):
    EFFECTIVE = 0
    INVALID = 1

    STATUS_TYPE = {
        EFFECTIVE: u"有效",
        INVALID: u"失效"
    }

    team = models.ForeignKey(CombatTeam, verbose_name=u"战队")
    request_member = models.ForeignKey(User, verbose_name=u"申请人")
    status = models.SmallIntegerField(verbose_name=u"信息状态", choices=STATUS_TYPE.items(), default=EFFECTIVE)
    created_at = models.DateTimeField(verbose_name=u"申请时间", auto_now_add=True, null=True)




