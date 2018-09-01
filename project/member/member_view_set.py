# -*- coding: utf-8 -*-
#
# (c) 2013-2018 Wishtack
#
# $Id: $
#
from rest_framework import viewsets, serializers

from project.member.member import Member


class MemberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Member
        fields = ['first_name']


class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer
