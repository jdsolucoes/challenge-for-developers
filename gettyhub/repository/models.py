# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, IntegrityError
from django.contrib.postgres.fields import ArrayField

from libs.github import SearchRepository


class Repository(models.Model):
    """This is the definition of the Github repository"""

    repository_id = models.PositiveIntegerField(verbose_name=u"Repository ID")
    name = models.CharField(max_length=128, verbose_name=u'Repository name')
    url = models.URLField(verbose_name=u"Repository URL")
    language = models.CharField(max_length=32)
    tags = ArrayField(
        models.CharField(max_length=32),
        null=True, blank=True, unique=True
    )

    def __unicode__(self):
        return "Repo: {}".format(self.url)

    class Meta:
        ordering = ('repository_id',)

    @classmethod
    def clear_repositories(cls):
        cls.objects.all().delete()

    @classmethod
    def import_repositories(cls, username):
        """Import all starred repos from an user"""
        client = SearchRepository(username)
        starred_repos = client.get_starred()

        for repo in starred_repos:
            obj = cls(
                name=repo['name'],
                repository_id=repo['id'],
                url=repo['url']
            )
            try:
                obj.save()
            except IntegrityError:
                print "Error importing repository {name} {id}".format(**repo)

    def info(self):
        """Return some basic info of this repository"""
        return {
            'id': self.repository_id,
            'name': self.name,
            'language': self.language,
            'tags': list(self.tags),
            'url': self.url,
        }



