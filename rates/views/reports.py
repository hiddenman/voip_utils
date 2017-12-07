#from csv import Dialect
import csv
import re
import logging
from decimal import Decimal
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django import template
from django.contrib.admin.views.decorators import staff_member_required
from django.views.decorators.cache import cache_page
from voip_utils.rates.models import *
from voip_utils.rates.forms.reports import *

#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s %(levelname)s %(message)s',
#                    filename='./log/rateman.log')
FOURPLACES = Decimal(10) ** -4
# FIXME: move to utils
class csv_dialect_voip(csv.excel):
    delimiter = ';'

csv.register_dialect('voip', csv_dialect_voip)
# end of FIXME

@staff_member_required
def redirect_to_rateman(request):
    return HttpResponseRedirect('./rateman/')

@staff_member_required
def redirect_to_admin(request):
    return HttpResponseRedirect('./admin/')


@staff_member_required
def index(request):
    return render_to_response('admin/index.html',
                              context_instance=template.RequestContext(request))
@staff_member_required
@cache_page(60*5)
def rates_by_targets(request):
    # Assume that codes in areas are sorted
    # FIXME: All! Checks and so on
    if request.method == 'POST':
        form = RatesByTargetsForm(request.POST)        
        if (form.is_valid()):
            #logging.debug('In the rates_by_targets()')
            countries = Country.objects.all()
            code_manual = None
            code_manual_country = None
            code_manual_area = None
            rates_list = []
            operator_targets = []
            rates_by_targets_countries = []
            rate_operators = []
            # FIXME: catches
            # rates_all = Rate.objects.select_related()
            operator_targets_countries = []
            target_operator = form.cleaned_data['target_operator']
            price_markup = form.cleaned_data['price_markup']
            rate_on_date = form.cleaned_data['rate_on_date']
            code_exact = form.cleaned_data['code_exact']

            # Use selected rates operators or all of them if no one was selected
            if (len(form.cleaned_data['rate_operators'])!=0):
                rate_operators = form.cleaned_data['rate_operators']
            else:
                rate_operators = Operator.objects.all()
                
            rate_quality = form.cleaned_data['rate_quality']
            
            # Filter operator targets by price code from combobox or manual entered code, otherwise use all operator's targets
            # TODO: support for command separated or multiselected targets
            # FIXME: price_code combobox disabled
            # FIME: optimoze conditions
            if (form.cleaned_data['code_country'] is not None and form.cleaned_data['code_country'].strip() != '') and not  (form.cleaned_data['code_manual'] is not None and form.cleaned_data['code_manual'].strip() != ''):
                # Country was selected
                #logging.debug('Start loading countries 1')
                code_country = form.cleaned_data['code_country']
                #logging.debug('End loading countries 1')
                #logging.debug('Start loading targets 1')
                operator_targets = Target.objects.filter(target_operator=target_operator,
                                                               target_code__area_country=code_country).select_related()
                #logging.debug('End loading targets 1')
            else:
                # Code was neither selected nor entered, so use all targets
                #logging.debug('Start loading targets 2')
                operator_targets = Target.objects.filter(target_operator=target_operator).select_related()
                #logging.debug('End loading targets 2')
                
                # FIXME: optimize
            if (form.cleaned_data['code_manual'] is not None and form.cleaned_data['code_manual'].strip() != ''):
                # Code was typed manual
                code_manual = form.cleaned_data['code_manual'].strip()
                #logging.debug('Start looking for country 1')
                for country_iter in countries:
                    if (code_manual.startswith(str(country_iter.country_code)) == 1):
                        # Cut country from the fullcode
                        code_manual_country = country_iter
                        # Areacode will be the rest
                        code_manual_area = str(code_manual[len(str(code_manual_country.country_code)):]).strip()
                        break
                #logging.debug('End looking for country 1')
                if (code_manual_country is None):
                    # FIXME:
                    # Raise right error + write warning
                    raise Country.DoesNotExist(_('Country not found for code: ') + str(code_manual))

                # Check is it RE or plain code
                is_code_manual_area_re = (code_manual_area !='' and not code_manual_area.isdigit())
                # Get clear code_manual_area for targets select                
                code_manual_area_clear = code_manual_area.replace('%','').replace('_','')
                # Replace '%' by '.*' ('%' is used in AMBS, managers like it ;)
                # Replace _ by ?, we support regexps now
                code_manual_area = code_manual_area.replace('%','.*').replace('_','.')
                    
                code_manual_area = '^' + code_manual_area + '$'
                
                code_manual_area_re = re.compile(code_manual_area)
                # VERY FIXME!
                # This query assumes that all targets are separated by code

                if (is_code_manual_area_re):
                    #logging.debug('Start loading targets 3')
                    # FIXME: We must pass raw string (how do we do them from variable?)
                    #raise IOError(code_manual_area)
                    operator_targets = Target.objects.filter(target_operator=target_operator,
                                                                   target_code__area_country=code_manual_country,
                                                                   target_code__area_code__regex=code_manual_area).select_related()
                    #logging.debug('End loading targets 3')
                else:
                    #logging.debug('Start loading targets 4')
                    if (code_manual_area_clear != ''):
                        operator_targets = Target.objects.filter(target_operator=target_operator,
                                                                       target_code__area_country=code_manual_country,
                                                                       target_code__area_code=code_manual_area_clear).select_related()
                        
                    else:
                        operator_targets = Target.objects.filter(target_operator=target_operator,
                                                                       target_code__area_country=code_manual_country).select_related()
                        
                    #logging.debug('End loading targets 4')

            if (not operator_targets.count() > 0):
                # Operator doesn't have such targets
                return render_to_response('reports/no_such_target.html',
                                          {'form': form,
                                           'target_operator': target_operator},
                                          context_instance=template.RequestContext(request))
            

            #logging.debug('Got operator_targets: %d' % (operator_targets.count()))

            # Collect targets countries
            # FIXME: use dinstinct insted of this piece of shit
            #logging.debug('Start loading countries by targets 1')
            for operator_target_iter in operator_targets:
                try:
                    operator_targets_countries.index(operator_target_iter.target_code.area_country)
                except ValueError:
                    operator_targets_countries.append(operator_target_iter.target_code.area_country)

            #logging.debug('End loading countries by targets 1')
            rate_operators_list = []

            # First level filter
            # select all rates by all targets' countries and operator (if any)            
            #if (rate_operators[0] == '*'):
                #logging.debug('Start loading rates 1')
            #    rates_by_targets_countries = Rate.objects.filter(rate_code__area_country__in=operator_targets_countries,
            #                                                     rate_start_date__lte=rate_on_date,
            #                                                     rate_end_date__gte=rate_on_date).select_related()
                #logging.debug('End loading rates 1')
            #else:
                #logging.debug('Start loading rates 2')
                #for rate_operator_iter in rate_operators:
                #    try:
                #        rate_operators_list.append(Operator.objects.get(id=rate_operator_iter))
                #    except Operator.DoesNotExist:
                #        continue
                #logging.debug('Got rate operators in the list after search: %d %s' % (len(rate_operators), str(rate_operators_list[0])))

            if (len(rate_quality)!=0):
                rates_by_targets_countries = Rate.objects.filter(rate_operator__in=rate_operators,
                                        rate_code__area_country__in=operator_targets_countries,
                                        rate_quality__in=rate_quality,
                                        rate_start_date__lte=rate_on_date,
                                        rate_end_date__gte=rate_on_date).select_related()
            else:
                rates_by_targets_countries = Rate.objects.filter(rate_operator__in=rate_operators,
                                        rate_code__area_country__in=operator_targets_countries,
                                        rate_start_date__lte=rate_on_date,
                                        rate_end_date__gte=rate_on_date).select_related()

                #logging.debug('End loading rates 2')
                
            #logging.debug('Got rates_by_targets_countries: %d' % (rates_by_targets_countries.count()))
            
            rates_by_target_country = []
            previous_country = None
            for operator_target_iter in operator_targets:
                rates_by_target_code = []
                #rates_by_target_country = []
                #logging.debug('Start loading rates by target 1')
                if (previous_country is None):
                    rates_by_target_country = rates_by_targets_countries.filter(rate_code__area_country=operator_target_iter.target_code.area_country).select_related()
                    previous_country=operator_target_iter.target_code.area_country
                else:
                    if (previous_country!=operator_target_iter.target_code.area_country):
                        rates_by_target_country = rates_by_targets_countries.filter(rate_code__area_country=operator_target_iter.target_code.area_country).select_related()
                        previous_country=operator_target_iter.target_code.area_country
                #logging.debug('End loading rates by target 1')
                #logging.debug('Got rates_by_target_country: %d' % (rates_by_target_country.count()))
                # Now play with area codes
                #logging.debug('Start looking for areas 1')
                for rate_by_target_country_iter in rates_by_target_country:
                    if (rate_by_target_country_iter.rate_code.area_code == ''):
                        # If rate area code == ''
                        if (operator_target_iter.target_code.area_code == ''):
                            # If target area code == '' as rate area code
                            rates_by_target_code.append(rate_by_target_country_iter)
                            continue
                        else:
                            if (code_manual is None):
                                # Empty rate always matches any target area (countries are the same, of course)
                                # TODO: commaseparated targets support
                                if (not code_exact):
                                    # If checkbox code_exact is not selected
                                    rates_by_target_code.append(rate_by_target_country_iter)
                                continue
                            else:
                                # Price code is entered by hand
                                # If code_manual regexp matches the target and the rate
                                if (code_exact):
                                    if (is_code_manual_area_re):
                                        ###if ((code_manual_area_re.match(price_operator_target_iter.target_code.area_code) is not None)):
                                            # Rate area code matches entered area code
                                            rates_by_target_code.append(rate_by_target_country_iter)
                                else:
                                    rates_by_target_code.append(rate_by_target_country_iter)
                                    
                                continue
                    else:
                        # Rate area code isn't empty string
                        if (code_manual is None):
                            # TODO: commaseparated targets support
                            if (operator_target_iter.target_code.area_code == rate_by_target_country_iter.rate_code.area_code):
                                rates_by_target_code.append(rate_by_target_country_iter)
                        else:
                            # TODO: commaseparated targets support
                            if (is_code_manual_area_re):
                                ###if (code_manual_area_re.match(operator_target_iter.target_code.area_code) is not None ):
                                    if (code_exact):                                        
                                        if (operator_target_iter.target_code.area_code == rate_by_target_country_iter.rate_code.area_code):
                                            rates_by_target_code.append(rate_by_target_country_iter)
                                    else:
                                        if (operator_target_iter.target_code.area_code.startswith(rate_by_target_country_iter.rate_code.area_code) or
                                            rate_by_target_country_iter.rate_code.area_code.startswith(operator_target_iter.target_code.area_code)):
                                            rates_by_target_code.append(rate_by_target_country_iter)
                                        
                            else:
                                if (code_exact):
                                    if (code_manual_area_clear == operator_target_iter.target_code.area_code):
                                        if (operator_target_iter.target_code.area_code == rate_by_target_country_iter.rate_code.area_code):
                                            rates_by_target_code.append(rate_by_target_country_iter)
                                else:
                                    if (operator_target_iter.target_code.area_code.startswith(code_manual_area_clear)):
                                        if (operator_target_iter.target_code.area_code.startswith(rate_by_target_country_iter.rate_code.area_code) or
                                            rate_by_target_country_iter.rate_code.area_code.startswith(operator_target_iter.target_code.area_code)):
                                            rates_by_target_code.append(rate_by_target_country_iter)
                                
                                    
                                        # for rate_by_target_lvl1_iter_array_iter in rate_by_target_lvl1_iter.rate_code.area_code.split(','):
                                        #    if (code_manual_area_re.match(rate_by_target_lvl1_iter_array_iter) is not None):
                                        #        rates_by_target_code.append(rate_by_target_lvl1_iter) 
                                        #        break
                                        #
                #logging.debug('End looking for areas 1')
                #logging.debug('Got rates_by_target_code: %d' % (len(rates_by_target_code)))
                
                #logging.debug('Start comparing prices 1')
                if (len(rates_by_target_code) > 0):
                    for rate_by_target_code_iter in rates_by_target_code:
                        # FIXME: Round price to 4 places
                        if (price_markup >= 0): 
                            rate_price_increased = Decimal(Decimal(rate_by_target_code_iter.rate_price) + \
                                                   ((Decimal(rate_by_target_code_iter.rate_price)/100) * price_markup)).quantize(FOURPLACES)
                            if (Decimal(rate_by_target_code_iter.rate_price) != 0) and (rate_price_increased <= Decimal(operator_target_iter.target_price)):

                                if (operator_target_iter.target_code.area_name == ''):
                                    operator_target_iter.target_code.area_name = operator_target_iter.target_code.area_country.country_name

                                if (operator_target_iter.target_code_name != ''):
                                    operator_target_iter.target_code.area_name = operator_target_iter.target_code_name

                                # FIXME: Rename field, it's neither rate nor target
                                rates_list_entry = {
                                    'rate': rate_by_target_code_iter,
                                    'target': operator_target_iter,                                        
                                    'rate_operator': rate_by_target_code_iter.rate_operator,
                                    'rate_quality': dict(rate_by_target_code_iter.QUALITY_CHOICES)[rate_by_target_code_iter.rate_quality],
                                    'rate_code': rate_by_target_code_iter.rate_code,
                                    'target_code': operator_target_iter.target_code,                                        
                                    'rate_price': rate_by_target_code_iter.rate_price, 
                                    'rate_price_increased': rate_price_increased, 
                                    'target_volume': operator_target_iter.target_volume,
                                    'target_price': operator_target_iter.target_price
                                    }
                                rates_list.append(rates_list_entry)
                                #logging.debug('Got rates_list_entry: %s' % (str(rates_list_entry)))
                        else:
                            target_price_increased = Decimal(Decimal(operator_target_iter.target_price) + \
                                                     ((Decimal(operator_target_iter.target_price) / 100) * abs(price_markup))).quantize(FOURPLACES)
                            rate_price_increased = 0
                            if (Decimal(rate_by_target_code_iter.rate_price) != 0) and (Decimal(rate_by_target_code_iter.rate_price) <= target_price_increased):

                                if (operator_target_iter.target_code.area_name == ''):
                                    operator_target_iter.target_code.area_name = operator_target_iter.target_code.area_country.country_name

                                if (operator_target_iter.target_code_name != ''):
                                    operator_target_iter.target_code.area_name = operator_target_iter.target_code_name    
                                # Rename field, it's neither rate nor target
                                rates_list_entry = {
                                    'rate': rate_by_target_code_iter,
                                    'target': operator_target_iter,
                                    'rate_operator': rate_by_target_code_iter.rate_operator,
                                    'rate_quality': dict(rate_by_target_code_iter.QUALITY_CHOICES)[rate_by_target_code_iter.rate_quality],
                                    'rate_code': rate_by_target_code_iter.rate_code,
                                    'target_code': operator_target_iter.target_code,                                        
                                    'rate_price': rate_by_target_code_iter.rate_price, 
                                    'target_price': operator_target_iter.target_price,
                                    'rate_price_increased': rate_price_increased,
                                    'target_volume': operator_target_iter.target_volume
                                    }
                                rates_list.append(rates_list_entry)
                                #logging.debug('Got rates_list_entry: %s' % (str(rates_list_entry)))
                #logging.debug('End comparing prices 1')

            # FIXME: all the fuck :(
            if (request.POST.has_key('output_csv')):
                response_csv =  HttpResponse(mimetype='text/csv')
                response_csv['Content-Disposition'] = 'attachment; filename=rates_by_targets-%s-%s.csv' % (target_operator.operator_name,
                                                                                                          str(datetime.datetime.now().date()))                
                writer = csv.writer(response_csv, dialect='voip')
                # FIXME: unicode encoding
                #writer.writerow([_('Country'), _('Rate area code'), _('Target area code'), _('Target area name'), _('Target volume'),
                #                 _('Target price'), _('Our price'), _('Rate price'), _('Rate operator')])
                writer.writerow([('Country'), ('Rate area code'), ('Target area code'), ('Target area name'), ('Target volume'),
                                 ('Target price'), ('Our price'), ('Rate price'), ('Rate operator')])
                
                for rate in rates_list:
                    # FIXME: rename fields
                    writer.writerow([rate['rate_code'].area_country.country_code,
                                     rate['rate_code'].area_code,
                                     rate['target_code'].area_code,                                     
                                     rate['target_code'].area_name,
                                     rate['target_volume'],
                                     rate['target_price'],
                                     rate['rate_price'],
                                     rate['rate_price_increased'],
                                     rate['rate_operator'].operator_name,
                                     rate['rate_quality']
                                     ])
                return response_csv
            else:
                return render_to_response('reports/rates_by_targets_list.html',
                                          {'form': form, 
                                           'rates_list': rates_list, 
                                           'target_operator': target_operator
                                           },
                                          context_instance=template.RequestContext(request))
        else:
            return render_to_response('reports/rates_by_targets.html',
                                      {'form': form},
                                      context_instance=template.RequestContext(request))
    else:
        form = RatesByTargetsForm()
        # OperatorForm = form_for_model(Operator)
        # form = OperatorForm()
        return render_to_response('reports/rates_by_targets.html',
                                  {'form': form},
                                  context_instance=template.RequestContext(request))
