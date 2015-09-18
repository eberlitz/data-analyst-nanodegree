#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
import pprint
import re
import operator

OSMFILE = 'data/porto-alegre_brazil.osm'
postcode_re = re.compile(r'^\d{5}-\d{3}$', re.IGNORECASE)

def count_tags(osmfile):
    tags = {}
    osm_file = open(osmfile, "r")
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if 'k' in tag.attrib:
                    if tag.attrib['k'] in tags:
                        tags[tag.attrib['k']] += 1
                    else:
                        tags[tag.attrib['k']] = 1
        elem.clear() # discard the element
    return tags

def test():
    print '\r\n# Top 30 tag values:'
    tags = count_tags(OSMFILE)
    sorted_x = sorted(tags.items(), key=operator.itemgetter(1), reverse=True)
    pprint.pprint(sorted_x[0:30])
    


def correctPostcode(value):
    new_postcode = re.sub(r'(\d{5}).*?(\d{3}).*', r'\1-\2', value.encode("utf-8"));
    m = postcode_re.match(new_postcode)
    if m:
        return new_postcode
    return ''


def printPostcodesStats():
    stats = {"incorrects":0,"corrects":0}
    for event, elem in ET.iterparse(OSMFILE, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                
                if 'k' in tag.attrib and tag.attrib['k'] == 'addr:postcode' and tag.attrib['v'] != None:
                    value = tag.attrib['v'].encode("utf-8")
                    m = postcode_re.match(value)
                    if not m:
                        # postcodes.append(value)
                        # print(value)
                        stats["incorrects"]+= 1;
                        # print(correctPostcode(tag.attrib['v']))
                    else:
                        stats["corrects"]+=1;
        elem.clear() # discard the element
    return stats

if __name__ == '__main__':
    test()

    print '\r\n# Postcodes count:'
    stats = printPostcodesStats()
    pprint.pprint(stats)
