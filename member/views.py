# -*- coding: utf-8 -*-
import uuid
from datetime import datetime
from django.shortcuts import render, render_to_response
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from django.core.cache import cache

from models import User, Team
from combat_team import logics as combat_team_logics
from common.decorator import check_auth
from geetest import GeetestLib
from mysite import settings

GEETEST = GeetestLib(settings.PC_GEETEST_ID, settings.PC_GEETEST_KEY)
CACHE_KEY = settings.CACHE_KEY % 'HOUR_COUNT'
#注册
@csrf_exempt
def regist(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        mailbox = request.POST.get('mailbox')
        if username and password and mailbox and confirm_password:
            if password == confirm_password:
             User.objects.create(username=username, password=password, mailbox=mailbox)
             return HttpResponseRedirect('/member/login/')
    else:
        return render(request, 'register.html')


@csrf_exempt
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        if user_name and password:
            user = User.objects.filter(username=user_name, password=password)
            if user:
                # 比较成功，跳转index
                response = HttpResponseRedirect('/member/index/')
                # 将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username', user_name, 36000)
                return response
            else:
                # 比较失败，保留在login
                return HttpResponseRedirect('/member/login/')
    else:
        return render(request, 'login.html')

		
def geetest_initialization(request):
    user_id = str(uuid.uuid4())
    status = GEETEST.pre_process(user_id)
    if not request.session.session_key:
        return False, _(u"请刷新登陆页面后重试."), None
    cache.set(request.session.session_key, status, 3600)
    cache.set("%s%s" % (request.session.session_key, "_geetest_user_id"), user_id, 3600)

    if cache.get(request.session.session_key) == 1:
        cache.set(CACHE_KEY, cache.get(CACHE_KEY) + 1)

    return GEETEST.get_response_str()


def geetest_two_callback(request):
    challenge = request.POST.get(GEETEST.FN_CHALLENGE, '')
    validate = request.POST.get(GEETEST.FN_VALIDATE, '')
    seccode = request.POST.get(GEETEST.FN_SECCODE, '')
    user_id = cache.get("%s%s" % (request.session.session_key, "_geetest_user_id"))
    status = cache.get(request.session.session_key)

    if not user_id:
        return False

    if status:
        result = GEETEST.success_validate(challenge, validate, seccode, user_id)
    else:
        result = GEETEST.failback_validate(challenge, validate, seccode)

    return result
		
		
		
@check_auth
def index(request):
    return render_to_response('combat_team/teams.html', combat_team_logics.get_combat_team_data(request))


def logout(request):
    response = HttpResponseRedirect('/member/login')
    response.delete_cookie('username')
    return response

@check_auth
def user_information(request):
    username = request.COOKIES.get('username', '')
    users = User.objects.filter(username=username)
    return render_to_response('information.html', {'users': users})


@csrf_exempt
def set_information(request):
    if request.method == 'POST':
        name = request.COOKIES.get('username', '')
        username = request.POST.get('username')
        phone_number = request.POST.get('phone_number')
        weixin = request.POST.get('weixin')
        qq = request.POST.get('qq')
        introduce = request.POST.get('introduce')

        user = User.objects.filter(username=name).update(
                                                  username=username,
                                                  phone_number=phone_number,
                                                  weixin=weixin,
                                                  qq=qq,
                                                  introduce=introduce
                                                  )
        if user:
            return HttpResponseRedirect('/member/index/')

    return render_to_response('information.html', {'users': User.ogjects.filter(username=username)})

