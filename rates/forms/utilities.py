# -*- coding: utf-8 -*-y
import datetime
from django import forms
from django.utils.translation import ugettext as _,ugettext_lazy
from voip_utils.rates.models import *
from voip_utils.rates.converters import basic

class ConverterForm(forms.Form):
    # FIXME: Add filter= count()>0
    order_choices = [('default',_('default (code;name;price)'))]
    for iter in basic.FIELD_SPLITTERS.keys():
        order_choices.append((iter,ugettext_lazy(basic.FIELD_SPLITTERS[iter]['desc'])))
    rate_file = forms.FileField(label=_('File with rates'),help_text=_('Select file with rates to convert'))
    fields_order = forms.ChoiceField(choices=order_choices,
                                     label=_('Fields order'),
                                     help_text=_('Select fields order in the file'))
    do_translit = forms.BooleanField(required=False,initial=True,label=_('Transliterate destination names'),help_text=_('Check if you want to transliterate destination names'))
    do_reduce_ranges = forms.BooleanField(required=False,label=_('Reduce ranges'),help_text=_('Check if you want to reduce ranges like 79000-79999 to 79'))
    do_compact_codes = forms.BooleanField(required=False,label=_('Compact codes'),help_text=_('Check if you want to compact output codes like 790,791..799 to 79'))
