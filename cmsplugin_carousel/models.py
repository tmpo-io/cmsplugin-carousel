#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: jordi collell <jordi@tempointeractiu.cat>
# -------------------------------------------------------------------
'''
'''
# coding: utf-8
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext as _
from cms.models.pluginmodel import CMSPlugin
from djangocms_text_ckeditor.fields import HTMLField
from djangocms_text_ckeditor.models import Text


class Carousel(CMSPlugin):
    title = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return u"%s" % self.title
