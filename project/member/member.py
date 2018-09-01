# -*- coding: utf-8 -*-
#
# (c) 2013-2018 Wishtack
#
# $Id: $
#

from django.db import models


class Member(models.Model):

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
