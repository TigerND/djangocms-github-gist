# -*- coding: utf-8 -*-

from cms.models import CMSPlugin
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.utils.compat.dj import python_2_unicode_compatible


@python_2_unicode_compatible
class GistPluginModel(CMSPlugin):

    name = models.CharField('Name',
        null=True,
        blank=True,
        help_text=_(u'Name (optional)'),
        max_length=32,
    )

    gist_user = models.CharField('GitHub User',
        blank=False,
        default='',
        help_text=_(u'Please supply the username of the GitHub user'),
        max_length=32,
    )

    gist_id = models.CharField('Gist ID',
        blank=False,
        default='',
        help_text=_(u'Please supply the ID of the gist'),
        max_length=32,
    )

    filename = models.CharField('GitHub File',
        blank=True,
        default='',
        help_text=_(u'Optional. Supply a filename'),
        max_length=64,
    )
    
    def ident(self):
        return self.name if self.name else u'%(user)s %(id)s' % {
            'user': self.gist_user,
            'id': self.gist_id,
        }

    def __str__(self):
        return _(u'Github Gist: %(ident)s') % {
            'ident': self.ident(),
        }
