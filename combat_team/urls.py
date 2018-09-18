# coding: UTF-8
from django.conf.urls import url,include
from django.contrib import admin
from combat_team import views


urlpatterns = [
    url(r'^create/$', views.create),
    url(r'^join/$', views.join),
    url(r'^join_team/$', views.join_team),
    url(r'^team_request/$', views.team_request),
    url(r'^agree_join_request/$', views.agree_join_team_request),
    url(r'^refuse_join_request/$', views.refuse_join_team_request),
    url(r'^team_members/$', views.team_members),
    url(r'^delete_team_member/$', views.delete_team_member),
    url(r'^team_administration/$', views.team_administration),
    url(r'^team_dissolution/$', views.team_dissolution),
    url(r'^matching/$', views.team_matching),
]
