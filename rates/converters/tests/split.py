#!/usr/bin/python
import sys

field_orders = basic.FIELD_SPLITTERS.keys()

def splitter(in_str=''):
    return in_str.split(';')
in_str = 'a;b;c;d'

a={'func':splitter}
print a['func'](in_str)

fmt = {}
(fmt['aa'],fmt['bb'],fmt['cc'],fmt['dd'])=in_str.split(';')

print fmt
