# -*yy coding: utf-8 -*-
# TODO:
# Do we have to raise our own exceptions, collect errors etc. or just ignore all of these?
# FORMATS:
# country;areacode,areacode;areaname;price
# countryareacode,countryareacode;areaname;price
# country:areacode,areacode;areaname;price
# countryareacodepart1;areacodepart2,areacodepart2;
# country;areaname;price
# countryareacode,countryareacode;areaname;price

import re
import string
import logging
from decimal import Decimal
from django.utils.translation import ugettext as _
from django.utils.encoding import force_unicode, smart_unicode
from pytils import translit
from voip_utils import utils

__desc__ = 'Basic converters: Rate, Target and Country'
# English X and Russian Х
# FIXME: Replace with all non-ascii range, or may be with russian X in three codepages
CHARS_STRIP = 'XХ$'
# FIXME: Bad idea, but should work faster then loop
CHARS_REPLACE_CODE_FROM='!"#$%&\'()*+./;<=>?@[\]^_`{|}~'
CHARS_REPLACE_CODE_TO='                             '
CHARS_REPLACE_AREANAME_FROM='!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
CHARS_REPLACE_AREANAME_TO='                                '
CHARS_REPLACE_PRICE_FROM='!"#$%&\'()*+-/:;<=>?@[\]^_`{|}~'
CHARS_REPLACE_PRICE_TO='                              '

# Some defaults
FIELD_DELIMITER = ';'

FIELD_SPLITTERS = {'code_name':
                   {'desc':'code;name','func':'splitter_code_name','columns':3},                   
                   'code_name_price':
                   {'desc':'code;name;price','func':'splitter_code_name_price','columns':4},
                   'name_code_price':
                   {'desc':'name;code;price','func':'splitter_name_code_price','columns':4},
                   'price_code_name':
                   {'desc':'price;code;name','func':'splitter_price_code_name','columns':4},                   
                   'code_name_volume_price':
                   {'desc':'code;name;volume;price','func':'splitter_code_name_volume_price','columns':5},

                 }


class Rate(object):
    def splitter_code_name_price(self):
        if (self.raw_str.count(FIELD_DELIMITER) < self.columns - 1):
            (self.country,self.area_name,self.price) = self.raw_str.split(FIELD_DELIMITER)
            self.area_code = ''
        else:
            (self.country,self.area_code,self.area_name,self.price) = self.raw_str.split(FIELD_DELIMITER)
        # Workaround for Life:) and so on
        if ((self.country.count(':') > 0) or (self.area_code.count(':') > 0 )):
            if (self.area_name.count(':') > 0 ):
                raise AssertionError('Both area code and area name have colon, i don''t know what to do: ' + self.raw_str)
            else:
                self.raw_str = self.raw_str.replace(':',FIELD_DELIMITER)
                eval('self.' + self.splitter['func'])()
    def splitter_name_code_price(self):
        if (self.raw_str.count(FIELD_DELIMITER) < self.columns - 1):
            (self.area_name,self.country,self.price) = self.raw_str.split(FIELD_DELIMITER)
            self.area_code = ''
        else:
            (self.area_name,self.country,self.area_code,self.price) = self.raw_str.split(FIELD_DELIMITER)
        # Workaround for Life:) and so on
        if ((self.country.count(':') > 0) or (self.area_code.count(':') > 0 )):
            if (self.area_name.count(':') > 0 ):
                raise AssertionError('Both area code and area name have colon, i don''t know what to do: ' + self.raw_str)
            else:
                self.raw_str = self.raw_str.replace(':',FIELD_DELIMITER)
                eval('self.' + self.splitter['func'])()
    def splitter_price_code_name(self):
        if (self.raw_str.count(FIELD_DELIMITER) < self.columns - 1):
            (self.price,self.country,self.area_name) = self.raw_str.split(FIELD_DELIMITER)
            self.area_code = ''
        else:
            (self.price,self.country,self.area_code,self.area_name) = self.raw_str.split(FIELD_DELIMITER)                        
        # Workaround for Life:) and so on
        if ((self.country.count(':') > 0) or (self.area_code.count(':') > 0 )):
            if (self.area_name.count(':') > 0 ):
                raise AssertionError('Both area code and area name have colon, i don''t know what to do: ' + self.raw_str)
            else:
                self.raw_str = self.raw_str.replace(':',FIELD_DELIMITER)
                eval('self.' + self.splitter['func'])()
    def pre_split(self):
        # Move this replacement from there because destination name may contain Life:) and so on so we will break the splitter
        #self.raw_str = self.raw_str.replace(':',FIELD_DELIMITER)
        return
    def split(self):
        eval('self.' + self.splitter['func'])()
    def post_split(self):
        # FIXME: use variable for replace symbols
        self.country = self.country.split(',')
        self.country.reverse()
        self.area_code = self.area_code.split(',')
        #self.price = self.price.replace(',','.')
    def clean(self):
        # Replace all punctuations marks with space and delete them
        # For price we do not replace dot and comma with space
        transtable_code=string.maketrans(CHARS_REPLACE_CODE_FROM, CHARS_REPLACE_CODE_TO)
        transtable_areaname=string.maketrans(CHARS_REPLACE_AREANAME_FROM, CHARS_REPLACE_AREANAME_TO)
        transtable_price=string.maketrans(CHARS_REPLACE_PRICE_FROM, CHARS_REPLACE_PRICE_TO)
        country = []
        area_code = []
        for iterator in self.country:
            country.append(iterator.translate(transtable_code, CHARS_STRIP+string.whitespace).replace(' ', ''))
        self.country = country
        for iterator in self.area_code:
            area_code.append(iterator.translate(transtable_code, CHARS_STRIP+string.whitespace).replace(' ', ''))
        self.area_code = area_code
        if (len(self.country) > 1):
            try:
                while True:
                    self.country.remove('')
            except:
                pass
        if (len(self.area_code) > 1):
            try:
                while True:
                    self.area_code.remove('')
            except:
                pass            
        # FIXME: We can't delete whitespaces in the translate() because it will concatenate words so just clean double spaces and tabs
        # FIXME: Doesn't replace multiple doublespaces
        # FIXME: Hardcoded replaces for words are bad
        self.area_name=re.sub(r'\bcell\b', 'mobile', re.sub(r'  +', ' ', self.area_name.translate(transtable_areaname).lower().replace('\t', '').replace('pstn', '').replace('proper', 'fixed').replace('cellular', 'mobile').strip()))
        if (self.do_translit is True):
            try:
                self.area_name = translit.translify(smart_unicode(self.area_name,strings_only=True,errors='replace')).title()
            except ValueError:
                # We have stupid string
                self.area_name = smart_unicode(self.area_name,strings_only=True,errors='replace') .title()
        # AMBS only accepts dot as decimal delimeter
        self.price=self.price.translate(transtable_price, CHARS_STRIP+string.whitespace).replace(' ', '').replace(',','.')
        # FIXME: Move to post
        if ((self.price == '0') or (self.price == '0.0')):
            self.price = 'blocked'
    def convert(self):
        if self.price != 'blocked':
            try:
                self.price = Decimal(self.price)
            except:
                self.price = Decimal(0)
    def expand(self):
        area_code = []
        country = []
        for iterator in self.area_code:
            range_pair = iterator.split('-')
            if (len(range_pair) > 1):
                assert len(range_pair[0]) == len(range_pair[1])
                #FIXME: Check for ranges like 02-09 and append nulls if any
                nil_count_left=len(range_pair[0])-len(range_pair[0].lstrip('0'))
                nil_count_right=len(range_pair[1])-len(range_pair[1].lstrip('0'))
                if (self.do_reduce_ranges is True):
                    # Fails on 0-9
                    assert nil_count_left == nil_count_right
                    #
                    # Remove unnecessary decimals in ranges like 0000-9999
                    range1=range_pair[0]
                    range2=range_pair[1]
                    # Check only one for len, because they are equal length
                    while (range1.endswith('0')) and (range2.endswith('9')) and (len(range1)>1):
                        range1=range1[:-1]
                        range2=range2[:-1]
                    range_pair[0]=range1
                    range_pair[1]=range2
                range_array = range(int(range_pair[0]),int(range_pair[1]) + 1)
                for range_iter in range_array:
                    area_code.append(str(range_iter).rjust(nil_count_left+len(str(range_iter)), '0'))
            else:
                area_code.append(iterator)
        area_code.reverse()
        self.area_code = area_code
        for iterator in self.country:
            range_pair = iterator.split('-')
            if (len(range_pair) > 1):
                # FIXME: Check whether both parts of the range have equal quantity of symbols
                # FIXME: Doesn't work on 1-99
                assert len(range_pair[0]) == len(range_pair[1])
                #FIXME: Check for ranges like 02-09 and append nulls if any
                nil_count_left=len(range_pair[0])-len(range_pair[0].lstrip('0'))
                nil_count_right=len(range_pair[1])-len(range_pair[1].lstrip('0'))
                assert nil_count_left == nil_count_right
                if (self.do_reduce_ranges is True):
                    # Remove unnecessary decimals in ranges like 0000-9999
                    range1=range_pair[0]
                    range2=range_pair[1]
                    # Check only one for len, because they are equal length
                    while (range1.endswith('0')) and (range2.endswith('9')) and (len(range1)>1):
                        range1=range1[:-1]
                        range2=range2[:-1]
                    range_pair[0]=range1
                    range_pair[1]=range2
                range_array = range(int(range_pair[0]),int(range_pair[1]) + 1)
                for range_iter in range_array:
                    country.append(str(range_iter).rjust(nil_count_left+len(str(range_iter)), '0'))
            else:
                country.append(iterator)
        country.reverse()
        self.country = country
        
    def validate(self):
        # FIXME: replace assert with something good
        assert self.country is not None
        assert type(self.country) is list
        for iterator in self.country:
            assert iterator is not None
            assert iterator != ''
            assert iterator.isdigit()
        assert self.area_code is not None
        assert type(self.area_code) is list
        if not ((len(self.area_code) == 1) and (self.area_code[0] == '')):
            for iterator in self.area_code:
                assert iterator is not None
                assert iterator != ''
                assert iterator.isdigit()
        assert self.area_name is not None
        assert (type(self.area_name) is str) or (type(self.area_name) is unicode)
        assert self.area_name !=''
        assert self.price is not None
        if self.price != 'blocked':
            assert type(self.price) is Decimal
    def init(self):
        self.columns = self.splitter['columns']        
        self.country = None
        self.area_code = None
        self.area_name = None
        self.price = None
    def __init__(self,raw_str='',splitter=FIELD_SPLITTERS['code_name_price'],do_translit=True,do_reduce_ranges=False):
        self.raw_str = raw_str.strip()
        self.splitter = splitter
        self.errors = []
        self.do_translit = do_translit
        self.do_reduce_ranges = do_reduce_ranges
        self.init()
        if (self.raw_str != ''):
            self.pre_split()
            self.split()
            self.post_split()
            self.clean()
            self.convert()
            self.expand()
            self.validate()
            self.cindex = len(self.country)
            if (self.cindex > 0):
                self.cindex -= 1
            self.aindex = len(self.area_code)
            if (self.aindex > 0):
                self.aindex -= 1                            
    def __iter__(self):
        return self
    def next(self):
        """Return expanded and cleaned string"""
        if (self.raw_str == ''):
            raise StopIteration
        if (self.cindex == -1) and (self.aindex == -1):
            raise StopIteration
        return_cortege = (self.country[self.cindex],self.area_code[self.aindex],self.area_name,self.price)        
        if (self.aindex >= 0):
            self.aindex -= 1
        if (self.aindex == -1) and (self.cindex >= 0):
            self.cindex -= 1
            if (self.cindex != -1):
                self.aindex = len(self.area_code) - 1
        return return_cortege

class Target(Rate):
    def splitter_code_name_volume_price(self):
        if (self.raw_str.count(FIELD_DELIMITER) < self.columns - 1):
            (self.country,self.area_name,self.volume,self.price) = self.raw_str.split(FIELD_DELIMITER)
            self.area_code = ''
        else:
            (self.country,self.area_code,self.area_name,self.volume,self.price) = self.raw_str.split(FIELD_DELIMITER)
        # Workaround for Life:) and so on
        if ((self.country.count(':') > 0) or (self.area_code.count(':') > 0 )):
            if (self.area_name.count(':') > 0 ):
                raise AssertionError('Both area code and area name have colon, i don''t know what to do: ' + self.raw_str)
            else:
                self.raw_str = self.raw_str.replace(':',FIELD_DELIMITER)
                eval('self.' + self.splitter['func'])()

    def init(self):        
        super(Target, self).init()
        self.columns = self.splitter['columns']
        self.volume = None
    def split(self):
        eval('self.' + self.splitter['func'])()        
    def post_split(self):
        super(Target, self).post_split()
        self.volume = self.volume.replace(',','.')        
    def convert(self):
        super(Target, self).convert()
        self.volume = Decimal(self.volume)
    def validate(self):
        super(Target, self).validate()
        assert self.volume is not None
        assert type(self.volume) is Decimal
    def __init__(self,raw_str='',splitter=FIELD_SPLITTERS['code_name_volume_price']):
        super(Target, self).__init__(raw_str,splitter)
    def next(self):
        """Return expanded and cleaned string"""
        if (self.raw_str == ''):
            raise StopIteration
        if (self.cindex == -1) and (self.aindex == -1):
            raise StopIteration
        return_cortege = (self.country[self.cindex],self.area_code[self.aindex],self.area_name,self.volume,self.price)        
        if (self.aindex >= 0):
            self.aindex -= 1
        if (self.aindex == -1) and (self.cindex >= 0):
            self.cindex -= 1
            if (self.cindex != -1):
                self.aindex = len(self.area_code) - 1
        return return_cortege

class Country(Rate):
    def splitter_code_name(self):
        if (self.raw_str.count(FIELD_DELIMITER) < self.columns - 1):
            (self.country,self.area_name) = self.raw_str.split(FIELD_DELIMITER)
            self.area_code = ''
        else:
            (self.country,self.area_code,self.area_name) = self.raw_str.split(FIELD_DELIMITER)
    def init(self):        
        super(Country, self).init()
        self.columns = self.splitter['columns']        
    def __init__(self,raw_str='',splitter=FIELD_SPLITTERS['code_name']):
        super(Country, self).__init__(raw_str,splitter)        
    def split(self):
        eval('self.' + self.splitter['func'])()                
    def post_split(self):
        # FIXME: use variable for replace symbols
        self.country = self.country.split(',')
        self.country.reverse()
    def clean(self):
        # Replace all punctuations marks with space and delete them
        # For price we do not replace dot and comma with space
        transtable_code=string.maketrans(CHARS_REPLACE_CODE_FROM, CHARS_REPLACE_CODE_TO)
        transtable_areaname=string.maketrans(CHARS_REPLACE_AREANAME_FROM, CHARS_REPLACE_AREANAME_TO)
        country = []
        for iterator in self.country:
            country.append(iterator.translate(transtable_code, CHARS_STRIP+string.whitespace).replace(' ', ''))
        self.country = country
        if (len(self.country) > 1):
            try:
                while True:
                    self.country.remove('')
            except:
                pass
        # FIXME: We can't delete whitespaces in the translate() because it will concatenate words so just clean double spaces and tabs
        # FIXME: Doesn't replace multiple doublespaces
        self.area_name=re.sub(r'\bcell\b', 'mobile', re.sub(r'  +', ' ', self.area_name.translate(transtable_areaname).lower().replace('\t', '').replace('pstn', '').replace('proper', 'fixed').replace('cellular', 'mobile').strip()))
        if (self.do_translit is True):
            try:
                self.area_name = translit.translify(smart_unicode(self.area_name,strings_only=True,errors='replace')).title()
            except ValueError:
                # We have stupid string
                self.area_name = smart_unicode(self.area_name,strings_only=True,errors='replace') .title()
    def convert(self):
        pass
    def expand(self):
        pass
    def validate(self):
        assert self.country is not None
        assert type(self.country) is list
        for iterator in self.country:
            assert iterator is not None
            assert iterator != ''
            assert iterator.isdigit()
        assert self.area_name is not None
        assert (type(self.area_name) is str) or (type(self.area_name) is unicode)
        assert self.area_name !=''
    def __init__(self,raw_str='',splitter=FIELD_SPLITTERS['code_name']):
        self.raw_str = raw_str.strip()
        self.splitter = splitter        
        self.init()
        if (self.raw_str != ''):
            self.pre_split()
            self.split()
            self.post_split()
            self.clean()
            self.convert()
            self.expand()
            self.validate()
            self.cindex = len(self.country)
    def next(self):
        """Return expanded and cleaned string"""
        if (self.raw_str == ''):
            raise StopIteration
        if (self.cindex == 0):
            raise StopIteration
        if (self.cindex > 0):
            self.cindex -= 1
        return (self.country[self.cindex],self.area_name)        
