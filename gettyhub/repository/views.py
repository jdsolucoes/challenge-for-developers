# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from repository.models import Repository
from repository.serializers import RepositorySerializer


def index(request):
    """Landpage"""
    return render(request, 'index.html')


class RepositoryView(APIView):
    """Repository's main view"""

    def get(self, request, repository_id=None):
        tag = request.GET.get('tag')
        repos = Repository.objects.all()
        if tag:
            repos = repos.filter(tags__icontains=tag)
        if repository_id:
            repos = repos.filter(repository_id=repository_id)

        serializers = RepositorySerializer(repos, many=True)

        return Response(serializers.data)

    def patch(self, request, repository_id):
        """Add or remove a tag from a repository"""
        repository = get_object_or_404(Repository, repository_id=repository_id)
        serializer = RepositorySerializer(
            repository, data=request.data, partial=True)
        if serializer.is_valid():
            repository = serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



