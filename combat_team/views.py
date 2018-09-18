# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from models import User
from combat_team.models import TeamRequest, CombatTeam
from combat_team import logics as combat_team_logics
from common.decorator import check_auth


@csrf_exempt
@check_auth
def create(request):
    if request.method == 'POST':
        status, message = combat_team_logics.create(request)
        if status:
            return HttpResponseRedirect("/member/index/")

    user_name = request.COOKIES.get('username', '')
    member = User.objects.get(username=user_name)
    combat_team = CombatTeam.objects.filter(leader=member)
    if not combat_team:
        return render_to_response('combat_team/create.html', combat_team_logics.get_game_type_data(request))
    else:
        return HttpResponseRedirect("/member/index")


@csrf_exempt
@check_auth
def join(request):
    return render_to_response('combat_team/join.html', combat_team_logics.get_combat_team_join_data(request))


@csrf_exempt
@check_auth
def join_team(request):
    if request.method == 'POST':
        status = combat_team_logics.set_combat_team_join_data(request)
        if status == True:
            return HttpResponseRedirect('/member/index')

    return render(request, 'combat_team/join.html',
                  {"teams": status["teams"],
                   "users": status["users"]},
                  )


@check_auth
def team_request(request):
    return render_to_response('combat_team/TeamRequest.html', combat_team_logics.get_team_request_data(request))


@check_auth
def agree_join_team_request(request):
    return render_to_response('combat_team/TeamRequest.html', combat_team_logics.agree_join_team_request(request))


@check_auth
def refuse_join_team_request(request):
    return render_to_response('combat_team/TeamRequest.html', combat_team_logics.refuse_join_team_request(request))


@check_auth
def team_members(request):
    return render_to_response('combat_team/TeamMember.html', combat_team_logics.get_team_members(request))


@check_auth
def delete_team_member(request):
    return render_to_response('combat_team/TeamMember.html', combat_team_logics.delete_team_members(request))


@check_auth
def team_administration(request):
    return render_to_response('combat_team/TeamAdministration.html',
                              combat_team_logics.get_team_administration_data(request)
                              )


@check_auth
def team_dissolution(request):
    return render_to_response('combat_team/TeamAdministration.html', combat_team_logics.get_team_dissolution(request))


@check_auth
def team_matching(request):
    status = combat_team_logics.get_team_matching(request)
    if status == True:
        return render_to_response('combat_team/StartGame.html')
    return HttpResponseRedirect('/member/index')

