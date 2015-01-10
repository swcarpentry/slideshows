#!/usr/bin/env python

'''Extract asides from slideshows.'''

import sys
import re
import xml.etree.cElementTree as et

with open(sys.argv[1], 'r') as reader:
    data = reader.read()
    data = re.sub('&[^;]+;', '', data)

xml = et.fromstring(data)
for thing in xml.findall('.//aside'):
    print '\n'.join([x.strip() for x in thing.text.strip().split('\n')])
    print
