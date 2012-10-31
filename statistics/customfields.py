# customfields.py

from django import forms
from django.conf import settings
from django.db import models
from django.template.loader import render_to_string

class ColorWidget(forms.Widget):

    def render(self, name, value, attrs=None):
        colors = settings.COLORPICKER_COLORS
        return render_to_string("color_widget.html", locals())

class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorWidget
        return super(ColorField, self).formfield(**kwargs)

