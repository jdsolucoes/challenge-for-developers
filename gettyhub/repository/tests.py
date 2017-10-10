# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from mock import patch
from rest_framework.test import APITestCase
from django.urls import reverse

from repository.models import Repository

# Create your tests here.

class RepositoryTest(APITestCase):

    FAKE_RESPONSE = [
        {
            'name': 'TesteRepo1',
            'url': 'http://google.com.br',
            'id': 1,
            'language': 'Python',
            'tags': ['show', 'top', 'massa']
        },
    ]

    def test_empty_repositories(self):
        total = Repository.objects.count()

        url = reverse('repository')
        response = self.client.get(url, format='json')

        self.assertEqual(total, 0)
        self.assertEqual(response.data, [])

    def test_repository_info(self):
        repo_id = 2332
        info = {
            'name': 'TesteRepo',
            'url': 'http://google.com.br',
            'repository_id': repo_id,
            'language': 'Python',
            'tags': ['show', 'top', 'massa']
        }
        # creating the db
        Repository.objects.create(**info)
        url = reverse('repository', kwargs={'repository_id': repo_id})
        response = self.client.get(url)
        # shoud be the same info, byt inside a list
        self.assertEqual([info], response.json())

    @patch('repository.models.SearchRepository.get_starred',
           return_value=FAKE_RESPONSE)
    def test_import_repository(self, obj):
        self.assertEqual(Repository.objects.count(), 0)
        Repository.import_repositories('teste')
        self.assertEqual(Repository.objects.count(), 1)



