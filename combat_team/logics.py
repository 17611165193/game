# -*- coding: utf-8 -*-
import time

from datetime import datetime
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from models import User
from combat_team.models import CombatTeam, CombatTeamMembers, TeamRequest, GameType


def create(request):
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    slogan = request.POST.get('slogan')
    type_id = request.POST.get('type_name')
    user_name = request.COOKIES.get('username', '')
    game_type = GameType.objects.get(id=type_id)

    if not user_name and game_type:
        return False

    if not name:
        return False, u"战队名为必选项"

    CombatTeam.objects.create(leader=User.objects.get(username=user_name), name=name,
                              phone_number=phone_number, slogan=slogan, type=game_type)

    return True, u"创建成功"


def get_game_type_data(request):

    return {
        'games': GameType.objects.filter()
    }


def get_combat_team_data(request):
    username = request.COOKIES.get('username', '')
    user = User.objects.get(username=username)

    if not user:
        return False

    return {
        'teams': CombatTeam.objects.filter(),
        'team': CombatTeam.objects.filter(leader_id=user.id)
    }


def get_combat_team_join_data(request):
    username = request.COOKIES.get('username', '')
    combat_team_id = request.GET.get('id')

    return {
        'teams': CombatTeam.objects.filter(id=combat_team_id),
        'users': User.objects.filter(username=username),
        'team_members': CombatTeamMembers.objects.filter(combat_team_id=combat_team_id)
    }


def set_combat_team_join_data(request):
    leader = request.GET.get('leader')
    username = request.COOKIES.get('username', '')
    combat_team_id = request.POST.get('combat_team_id')
    member = User.objects.get(username=username)
    team = CombatTeam.objects.get(id=combat_team_id)

    data = {
        'teams': CombatTeam.objects.filter(id=combat_team_id),
        'users': User.objects.filter(username=username),
    }
    if username == leader:
        return data

    TeamRequest.objects.create(team=team, request_member=member)

    return True


def get_team_request_data(request):
    team_id = request.GET.get('team_id')
    return {
        'team_request': TeamRequest.objects.filter(team_id=team_id, status=TeamRequest.INVALID),
    }


def agree_join_team_request(request):
    member_id = request.GET.get('member_id')
    team_id = request.GET.get('team_id')
    member = User.objects.get(id=member_id)
    team = CombatTeam.objects.get(id=team_id)
    TeamRequest.objects.filter(request_member_id=member_id, team_id=team_id).delete()
    CombatTeamMembers.objects.create(combat_team=team, member=member)
    return{
        'team_request': TeamRequest.objects.filter(team_id=team_id),
    }


def refuse_join_team_request(request):
    member_id = request.GET.get('member_id')
    team_id = request.GET.get('team_id')
    TeamRequest.objects.filter(request_member_id=member_id, team_id=team_id).delete()
    return {
        'team_request': TeamRequest.objects.filter(team_id=team_id),
    }


def get_team_members(request):
    username = request.COOKIES.get('username', '')
    user = User.objects.get(username=username)
    team = CombatTeam.objects.get(leader_id=user.id)

    return{
        'team_members': CombatTeamMembers.objects.filter(combat_team_id=team.id)
    }


def delete_team_members(request):
    team_id = request.GET.get('team_id')
    member_id = request.GET.get('member_id')
    username = request.COOKIES.get('username', '')
    user = User.objects.get(username=username)
    team = CombatTeam.objects.get(leader_id=user.id)
    CombatTeamMembers.objects.filter(combat_team_id=team_id, member_id=member_id).delete()
    return{
        'team_members': CombatTeamMembers.objects.filter(combat_team_id=team.id)
    }


def get_team_administration_data(request):
    username = request.COOKIES.get('username', '')
    users = User.objects.get(username=username)
    return{
        'teams': CombatTeam.objects.filter(leader_id=users.id)
    }


def get_team_dissolution(request):
    team_id = request.GET.get('team_id')
    username = request.COOKIES.get('username', '')
    users = User.objects.get(username=username)
    CombatTeam.objects.filter(id=team_id).delete()
    CombatTeamMembers.objects.filter(combat_team_id=team_id).delete()
    return{
        'teams': CombatTeam.objects.filter(leader_id=users.id)
    }


def get_team_matching(request):
    team_id = request.GET.get('team_id')
    type_id = request.GET.get('type_id')
    username = request.COOKIES.get('username', '')
    user = User.objects.get(username=username)
    leader = CombatTeam.objects.filter(leader_id=user.id).count()
    members = CombatTeamMembers.objects.filter(combat_team_id=team_id).count()
    game_members = GameType.objects.get(id=type_id)
    if leader + members != game_members.people_number:
        return False, u"战队人数不够"

    return True
