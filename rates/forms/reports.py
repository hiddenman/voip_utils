from django import forms
from django.utils.translation import ugettext as _
from voip_utils.rates.models import *
import datetime
class RatesByTargetsForm(forms.Form):
    # First value will be the default
    QUALITY_CHOICES = (
    ('N', 'Normal or Unknown'),
    ('P', 'Premium'),
    ('D', 'Direct')
   )
    # FIXME: Add filter= count()>0
    target_operator = forms.ModelChoiceField(queryset=Operator.objects.filter(target__isnull=False).distinct(),
                                             label=_('Analyse targets of operator'),
                                             help_text=_('Select operator to analyse its targets'))
    rate_operators = forms.ModelMultipleChoiceField(queryset=Operator.objects.filter(rate__isnull=False).distinct(),
                                                    label=_('Use rates of operator'),
                                                    help_text=_('You can select multiple operators or choose no one to use all of them'),
                                                    required=False)
    rate_quality = forms.MultipleChoiceField(required=False,choices=QUALITY_CHOICES,
                                                  label=_('Choose rate quality to search for'),
                                                help_text=_('Do not choose anything to use all rate types'))
    rate_on_date = forms.DateField(initial=lambda : datetime.datetime.now().date(),
                                   label=_('Rate on date'),
                                   help_text=_('Use rate which works on this date'))
    #price_rate_end_date = forms.DateField(initial=datetime.datetime.max.date())
    # FIXME: temporarily disabled Area
    #price_code = forms.ModelMultipleChoiceField(queryset=Area.objects.all(), required=False)
    # FIXME
    # How do we use only country names, not code?
    code_country = forms.ModelChoiceField(queryset=Country.objects.all(),
                                          required=False,
                                          label=_('Choose country'),
                                          help_text=_('Or choose country'))
    code_manual = forms.CharField(required=False,
                                  label=_('Area code'),
                                  help_text=_('You can enter code or subcode (use % and _ as mask symbols)'))
    code_exact = forms.BooleanField(required=False,
                                    label=_('Exact area code'),
                                    help_text=_('Display only matched codes'))
    price_markup = forms.DecimalField(initial='5.0',
                                      max_digits=8,
                                      decimal_places=4,
                                      label=_('Percent of the price as markup'),
                                      help_text=_('Add this percent of the original price to the final price and compare them. You can use negative values'))
