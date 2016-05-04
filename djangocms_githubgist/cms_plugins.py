# -*- coding: utf-8 -*-

from django.conf import settings

from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import GistPluginModel
from .forms import GistPluginAdminForm

from django.utils.translation import ugettext_lazy as _


class GithubGistPlugin(CMSPluginBase):
    form = GistPluginAdminForm
    name = _('Gist')
    module = _('Github')
    model = GistPluginModel
    render_template = "djangocms_githubgist/gist.html"
    text_enabled = True

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context

    def icon_src(self, instance):
        # //img.shields.io/badge/plugin-github%20gist-green.svg
        return settings.STATIC_URL + 'djangocms_githubgist/plugin-github%20gist-green.svg'

    def icon_alt(self, instance):
        return u'Github Gist: %s' % instance


plugin_pool.register_plugin(GithubGistPlugin)
