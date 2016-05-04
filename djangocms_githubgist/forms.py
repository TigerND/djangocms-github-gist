# -*- coding: utf-8 -*-

from django import forms
from django.forms.models import ModelForm

from .models import GistPluginModel

from django.utils.translation import ugettext_lazy as _


class GistPluginAdminForm(ModelForm):

    class Meta:
        model = GistPluginModel
        exclude = ()

    def __init__(self, *args, **kwargs):
        super(GistPluginAdminForm, self).__init__(*args, **kwargs)
