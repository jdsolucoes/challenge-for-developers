# -*- coding: utf-8 -*-
from rest_framework import serializers

from repository.models import Repository


class RepositorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Repository
        fields = ['repository_id', 'name', 'url', 'language', 'tags']

    def validate_tags(self, value):
        """Remove duplicated tags"""
        unique = set(value)
        return list(unique)
