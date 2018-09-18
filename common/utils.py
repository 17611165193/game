# coding: UTF-8
import yaml
import datetime
import urllib
import json
import httplib
import hashlib
import time
import random
import string
import pickle
import urllib2
import functools

from decimal import Decimal
from json import JSONDecoder
from django.conf import settings
from django.core.cache import cache
from django.http import JsonResponse
from django.shortcuts import render
from collections import OrderedDict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.hashers import make_password as django_make_password, check_password as django_check_password
from django.utils.translation import ugettext as _

YUNPIAN_API_KEY = '0abc515d35e5c025c949fe319a577c8c'

def get_md5_image_name(filename=None):
    """
    md5加密图片名
    """
    suffix = 'jpg'  # default
    if filename:
        _suffix = str(filename.split('.')[-1])
        if _suffix.lower() in ('jpg', 'jpeg', 'png', 'bmp'):
            suffix = _suffix

    md5_avatar_name = hashlib.md5("%s_%s" % (
        time.time(), random.randrange(1, 9999999))).hexdigest()

    return '{}.{}'.format(md5_avatar_name, suffix)


def send_yunpian_message(phone_number, **data):
    """
    发送yunpian验证码
    phone_number: 接受短信手机号
    data:
        message_type: 验证码类别

    test:
        验证码类:
            from common import utils
            utils.send_yunpian_message('13521296223', code='888888')
    """
    if getattr(settings, 'LOCAL', False) or getattr(settings, 'DEV', False):
        print "local....", data
        return True

    message_type = data.get('message_type', u'common')

    message_types = {
        u"member_register_count_warning": (YUNPIAN_API_KEY, u"今日新增用户:%(event_name)s,请登录到管理后台查询"),
    }

    text = message_types[message_type][1] % data
    params = {
        'apikey': message_types[message_type][0].encode('utf-8'),
        'mobile': str(phone_number).encode('utf-8'),
        'text': text.encode('utf-8'),
    }

    print text

    host = settings.SMS_HOST
    url = settings.SMS_URL

    headers = {
        'User-Agent': u'python',
        'Content-Type': u'application/x-www-form-urlencoded; charset=UTF-8',
    }

    values = urllib.urlencode(params)
    try:
        conn = httplib.HTTPSConnection(host)
        conn.request("POST", url, values, headers)
        response = conn.getresponse()
        data = response.read()
        #print phone_number, 'Response: ', response.status, response.reason, 'Data:', data
        json_data = JSONDecoder().decode(data)
        if json_data.get('code') == 0 and json_data.get('msg') == 'OK':
            return True
    except Exception, e:
        print '[error SMS] : 发送短信失败: %s' % e
    return False