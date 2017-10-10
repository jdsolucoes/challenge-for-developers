# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

from django.core.management.base import BaseCommand

from repository.models import Repository



class Command(BaseCommand):
    help = 'Import all starred repos from a single user'

    def handle(self, *args, **kwargs):
        username = raw_input('Github username: ')
        print('Importing...')
        Repository.clear_repositories()
        Repository.import_repositories(username)

