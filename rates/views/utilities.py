# -*- coding: utf-8 -*-
#from csv import Dialect
import ordereddict
import csv
import operator
import re
import logging
import StringIO
from decimal import Decimal
from django.utils.translation import ugettext as _
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django import template
from django.contrib.admin.views.decorators import staff_member_required
from voip_utils.rates.models import *
from voip_utils.rates.forms.utilities import *

logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s %(levelname)s %(message)s',
                    filename='./log/rateman.log')




def addOne(foundPrefix, prefix, name, price):
    prefixList = foundPrefix.setdefault((name, price), [])
    prefixList.append(prefix)

def addAll(priceList):
    foundPrefix = {}
    for price in priceList.keys():
        addOne(foundPrefix, price, priceList[price][0], priceList[price][1])

    return foundPrefix


def checkPrefix(prefixList):
    differentPrefixMap = {}
    for prefix in prefixList:
        prefixPattern = str(prefix)[:-1]
        lastPrefixDigit = int(str(prefix)[-1])
        differentPrefixMap.setdefault(prefixPattern, set()).update((lastPrefixDigit,))

    wrongPrefixList = []
    for prefix, lastDigitSet in differentPrefixMap.items():
        if len(lastDigitSet) == 10:
            wrongPrefixList.append(prefix)

    return wrongPrefixList

def checkForRange09(priceList):
    foundPrefix = addAll(priceList)
    wrongPrefix = []
    for key, prefixList in foundPrefix.items():
        # Optimization: if less then 10 prefix was found there are no all last 0-9 digits
        if len(prefixList) >= 10:
            wrong = checkPrefix(prefixList)
            if wrong:
                wrongPrefix.append((wrong, key))

    return wrongPrefix

def convertRates(rates=[]):
    return rates
# FIXME: move to utils
class csv_dialect_voip(csv.excel):
    delimiter = ';'

csv.register_dialect('voip', csv_dialect_voip)
# end of FIXME

@staff_member_required
def converter(request):
    # Assume that codes in areas are sorted
    # FIXME: All! Checks and so on
    if request.method == 'POST':
        form = ConverterForm(request.POST, request.FILES)
        if (form.is_valid()):
            # FIXME: all the fuck :(
            splitter = form.cleaned_data['fields_order']
            do_translit = form.cleaned_data['do_translit']
            do_reduce_ranges = form.cleaned_data['do_reduce_ranges']
            do_compact_codes = form.cleaned_data['do_compact_codes']
            if (splitter == 'default'):
                # FIXME: hardcoded
                splitter = 'code_name_price'

            if (len(form.cleaned_data['rate_file'])!=0):
                response_csv =  HttpResponse(mimetype='text/csv')
                response_csv['Content-Disposition'] = 'attachment; filename=rates-%s.csv' % (str(datetime.datetime.now().date()))
                writer = csv.writer(response_csv, dialect='voip')
                #writer.writerow([unicode(_('Area code'),'utf-8','ignore'),unicode(_('Area name'),'utf-8','ignore'),unicode(_('Area price'),'utf-8','ignore')])
                #writer.writerow([unicode(_('Area code')),unicode(_('Area name')),unicode(_('Area price'))])
                #writer.writerow([_('Area code'),_('Area name'),_('Area price'с)])
                if (request.FILES.has_key('rate_file')):
                    if (request.FILES['rate_file'].size >0):
                        rates = request.FILES['rate_file'].readlines()
                        rates_out = ordereddict.OrderedDict()
                        rates_converted = ()
                        is_rates_valid = False
                        for rate_iter in rates:
                            for (area_country,area_code,area_name,area_price) in basic.Rate(raw_str=rate_iter,splitter=basic.FIELD_SPLITTERS[splitter],do_translit=do_translit,do_reduce_ranges=do_reduce_ranges):
                                # Check for dups
                                if ((str(area_country)+str(area_code))) in rates_out:
                                    raise LookupError('Found duplicated string: '+str(rate_iter))
                                    # FIXME: Don't need, but don't forget later
                                    break
                                else:
                                    rates_out[(str(area_country)+str(area_code))] = (area_name, area_price)
                        # Sort rates by area name
                        #rates_out = sorted(rates_out,key=operator.itemgetter(1))
                        # FIXME: Workaround for ranges 0-9, we have to replace them
                        while (is_rates_valid == False):
                            ranges09 = checkForRange09(rates_out)
                            if len(ranges09)>0:
                                # So we've found ranges 0-9 with the same name, change the areaname for code 0 or
                                # replace them with shorter code if do_compact_codes
                                # raise LookupError('Found ranges 0-9 with same name and price: '+str(ranges09[0][0]))
                                keys_to_delete = set()
                                for range_iter in ranges09:
                                    for code_iter in range_iter[0]:
                                        if (do_compact_codes is True):
                                            for num_iter in range(0,10):
                                                keys_to_delete.add(str(code_iter)+str(num_iter))
                                        else:
                                            rates_out[str(code_iter)+'0']=(range_iter[1][0]+' 0', range_iter[1][1])
                                if (do_compact_codes is True):
                                    #rates_out2 = ordereddict.OrderedDict([(str(code_iter), v) if k == str(code_iter)+'0' else (k, v) for k, v in rates_out.items() if k not in keys_to_delete])
                                    rates_out2 = ordereddict.OrderedDict()
                                    for k, v in rates_out.items():
                                        if k in keys_to_delete and k.endswith('0'):
                                             rates_out2[k[:-1]] = v
                                        elif k not in keys_to_delete:
                                            rates_out2[k] = v
                                    rates_out = rates_out2
                                for row_iter in rates_out.keys():
                                    writer.writerow((row_iter, rates_out[row_iter][0],rates_out[row_iter][1]))
                                is_rates_valid = True
                            else:
                                for row_iter in rates_out.keys():
                                    writer.writerow((row_iter, rates_out[row_iter][0],rates_out[row_iter][1]))
                                is_rates_valid = True
                            #writer.writerow([area_country+area_code,area_name,area_price])
                return response_csv
            else:
                return render_to_response('utilities/converter.html',
                                          {'form': form,
                                           },
                                          context_instance=template.RequestContext(request))
        else:
            return render_to_response('utilities/converter.html',
                                      {'form': form},
                                      context_instance=template.RequestContext(request))
    else:
        form = ConverterForm()
        # OperatorForm = form_for_model(Operator)
        # form = OperatorForm()
        return render_to_response('utilities/converter.html',
                                  {'form': form},
                                  context_instance=template.RequestContext(request))
