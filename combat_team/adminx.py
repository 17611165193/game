# coding: UTF-8
import xadmin

from models import GameType

class GameTypeAdmin(object):

    list_display = ['id', 'name', 'people_number', 'created_at']
    search_fields = list_display = ['id', 'name', 'people_number']

xadmin.site.register(GameType,GameTypeAdmin)

