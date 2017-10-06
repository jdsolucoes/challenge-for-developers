# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.postgres.fields import ArrayField


class Repository(models.Model):
    """This is the definition of the Github repository"""

    repository_id = models.PositiveIntegerField(verbose_name=u"Repository ID")
    name = models.CharField(max_length=128, verbose_name=u'Repository name')
    url = models.URLField(verbose_name=u"Repository URL")
    language = models.CharField(max_length=32)
    tags = ArrayField(
        models.CharField(max_length=32),
        null=True, blank=True
    )

    def __unicode__(self):
        return "Repo: {}".format(self.url)
