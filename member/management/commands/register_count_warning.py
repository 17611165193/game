# coding=utf-8
"""
监控每日注册用户量
"""
import datetime

from django.core.management.base import BaseCommand
from member.models import User
from common import utils


class Command(BaseCommand):
    args = ""

    def handle(self, *args, **options):
        self.warning()

    def warning(self):
        add_member_count = User.objects.filter(created_at__gte=datetime.date.today()).count()
        if add_member_count >= 100:
            utils.send_yunpian_message('17717710151', count=add_member_count, message_type='member_register_count_warning')

        print u"当前新增用户", add_member_count
