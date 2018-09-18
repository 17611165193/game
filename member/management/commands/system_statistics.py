# coding: UTF-8
import datetime

from django.core.management.base import BaseCommand

from combat_team.models import TeamRequest


class Command(BaseCommand):
    args = ""

    def handle(self, *args, **options):
        self.team_request_invalid()

    def team_request_invalid(self):
        TeamRequest.objects.filter(created_at__date=(datetime.date.today() + datetime.timedelta(days=1)), status=TeamRequest.EFFECTIVE)\
                                          .update(status=TeamRequest.INVALID)
