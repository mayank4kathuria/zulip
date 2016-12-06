from __future__ import absolute_import
from __future__ import print_function

import subprocess

from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.conf import settings


class Command(BaseCommand):
    def handle(self, **options):
        # type: (**bool) -> None
        subprocess.check_call(['uwsgi', '--ini', '/etc/zulip/uwsgi.ini'])
