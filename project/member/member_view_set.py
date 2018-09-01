# -*- coding: utf-8 -*-
#
# (c) 2013-2018 Wishtack
#
# $Id: $
#

from rest_framework import serializers
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from ..lib.paginator import Paginator
from ..lib.token_authentication import TokenAuthentication
from ..member.member import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ['first_name']


class MemberViewSet(CreateAPIView, ListAPIView, ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    pagination_class = Paginator
