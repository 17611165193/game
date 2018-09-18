# coding: UTF-8

from django.shortcuts import render
from django.http import HttpResponseRedirect


def check_auth(func):
    def new_func(request, *args, **argw):
        if not request.COOKIES.get('username'):

            return render(request, 'login.html')

        return func(request, *args, **argw)

    return new_func