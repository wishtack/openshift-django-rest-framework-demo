# -*- coding: utf-8 -*-
#
# (c) 2013-2018 Wishtack
#
# $Id: $
#
from collections import OrderedDict

from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from project.member.member import Member


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


class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ['first_name']


class MemberViewSet(CreateAPIView, ListAPIView, ViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = Paginator
