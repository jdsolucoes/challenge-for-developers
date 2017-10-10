# -*- coding: utf-8 -*-
"""
A single purpose file for github access
"""

from __future__ import unicode_literals

import requests
import urllib


class SearchRepository(object):

    base_url = 'https://api.github.com/users'

    def __init__(self, username):
        """@username: The github username"""
        self.username = username

    def get_starred(self):
        """Get the starred repositories from a specific user"""
        return self.get('starred', sort="updated", direction="desc").json()

    def get(self, path, **kwargs):
        """URL builder"""
        url = "{}/{}/{}".format(self.base_url, self.username, path)

        # encode querystring
        if kwargs:
            url += '?{}'.format(urllib.urlencode(kwargs))
        return requests.get(url)
