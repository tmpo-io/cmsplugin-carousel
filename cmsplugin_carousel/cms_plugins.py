#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from django.utils.translation import ugettext_lazy as _

from cmsplugin_filer_image.cms_plugins import FilerImagePlugin

from .models import Carousel


class CarouselPlugin(CMSPluginBase):
    model = Carousel
    module = 'Filer'
    name = _("Carousel")
    render_template = "carousel.html"
    allow_children = True
    child_classes = ['CarouselImagePlugin']

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            'placeholder': placeholder,
        })
        return context


class CarouselImagePlugin(FilerImagePlugin):
    parent_classes = ['CarouselPlugin']
    render_template = "image.html"


plugin_pool.register_plugin(CarouselPlugin)
plugin_pool.register_plugin(CarouselImagePlugin)
