# coding: UTF-8
from django.conf.urls import url, include
from django.contrib import admin
import views

admin.autodiscover()

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^regist/$', views.regist, name='regist'),
    url(r'^index/$', views.index, name='index'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^information/$', views.user_information),
    url(r'^set_information/$', views.set_information),
]
