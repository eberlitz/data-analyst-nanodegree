#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint

OSMFILE = 'porto-alegre_brazil.osm'

def printPostcodes():
    for event, elem in ET.iterparse(OSMFILE, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                
                if 'k' in tag.attrib and tag.attrib['k'] == 'addr:postcode' and tag.attrib['v'] != None:
                    print(tag.attrib['v'].encode("utf-8"))
        elem.clear() # discard the element

if __name__ == '__main__':
    printPostcodes()
