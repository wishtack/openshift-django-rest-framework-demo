# -*- coding: utf-8 -*-
#
# (c) 2013-2018 Wishtack
#
# $Id: $
#
from collections import OrderedDict

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response


class Paginator(LimitOffsetPagination):

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('meta', {
                'total_count': self.count,
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            }),
            ('data', data)
        ]))
