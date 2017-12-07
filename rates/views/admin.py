from voip_utils.rates.models import Rate,Target
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import ugettext as _,ugettext_lazy
from voip_utils.rates.converters import basic

@staff_member_required
def add_rate(request):
    order_choices = [('default',_('default (code;name;price)'))]
    for iter in basic.FIELD_SPLITTERS.keys():
        order_choices.append((iter,ugettext_lazy(basic.FIELD_SPLITTERS[iter]['desc'])))
    return render_to_response(
        "admin/rates/rate/change_form.html",
        {'field_orders' : order_choices},
        RequestContext(request, {}),
    )
