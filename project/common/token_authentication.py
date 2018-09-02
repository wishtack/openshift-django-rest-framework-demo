# -*- coding: utf-8 -*-
#
# (c) 2013-2018 Wishtack
#
# $Id: $
#
from collections import namedtuple

from rest_framework import authentication, exceptions


class TokenAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):

        authorization_header = request.META.get('HTTP_AUTHORIZATION')

        if not authorization_header:
            return None

        token_list = authorization_header.split(',')
        if len(token_list) == 0:
            raise exceptions.AuthenticationFailed('Invalid authorization header')

        key, value = token_list[0].split(' ')

        user = None

        # Temporary stuff meanwhile we do a real implementation.
        if value == 'SECRET_TOKEN':
            User = namedtuple('User', ['first_name', 'is_authenticated', 'is_admin'])
            user = User(first_name='Foo', is_admin=True, is_authenticated=True)

        if user is None:
            raise exceptions.AuthenticationFailed('Invalid token')

        return (user, None)
