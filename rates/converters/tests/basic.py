#!/usr/bin/python
import sys
sys.path.append('../../../../')
from voip_utils.rates.converters import basic
from voip_utils import utils
ee = []
four = ()
five = ()
for (a,b,c,d) in basic.Rate('украина;380,370;0.01',splitter=basic.FIELD_SPLITTERS['name_code_price']):
    ee.append([a+b,c,d])
    print a,b,c,d
sys.exit()
for (a,b,c,d,e) in basic.Target('380;ukraine;999999999.999999999;0.01'):
    ee.append([a+b,c,d,e])
    print a,b,c,d,e
for (a,b) in basic.Country('380;97;ukraine'):
    print a,b
