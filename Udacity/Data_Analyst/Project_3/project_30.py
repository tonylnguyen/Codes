#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
from pymongo import MongoClient
from collections import defaultdict
import json

"""
To do list
[] - find any odd data (write code to find it)
    [x] - all cities
    [] - all streets
    [] - all keys
    [] - all counties?
[] -? convert the data into a dictionary
[] - use mongo DB to clean it up
"""


osmfile = '/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_3/Project_3/sample.osm'

data_file = open(osmfile, 'r')

iparse = ET.iterparse(osmfile, events=("start",))
parse = ET.parse(data_file)
root = parse.getroot()

expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons"]

mapping = {"St.": "Street",
           "St": "Street",
           "Rd": "Road",
           "Rd.": "Road",
           "Ave": "Avenue",
           "Ave.": "Avenue"}


lower = re.compile(r'^([a-z]|_)*$')  # returns all lower case keys
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')  # return all keys with :
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)


odd_streets = []
cities = []
city_count = {}
odd_streets_count = {}
street_use = defaultdict(set)



#The code below was used to extract all the data that contained a certian certian,
#but ater evaluating that data, there was an insufficient amount of data needed.
#The idea was scrapped.
#
mpk = root.iterfind(".//tag[@v='Redwood City']..") #find all values where v = palo alto, and find the parent

list2 = [1700520910,
2470625251,
2472221199,
2483021840,
2483023391,
2483026175,
239256902,
239257422,
239258036,
239262523,
239446902,
239448115,
240211505,
240212081,
240418729,
240423128,
240425342,
240428162,
240429594,
240430954,
240579234,
240579747,
240580339,
240580890,
240581615,
240582130,
240582665,
240583298,
240583862,
240584523,
240585533,
240593503,
240594036,
240594562,
]
list1 = []
for i in mpk: #for every parent
    dicto = {}
    parent = i.attrib #print parent (ways)
    for k,v in parent.items():
        if k == 'id':
            list1.append(int(v))
    # for t in i.iterfind('./'): #finds child (tags)
    #     child = t.attrib
    # lister.append(dicto)
#
# for i in list1:
#     if i not in list2:
#         print i



def elements(iparse):
    my_data = []
    for key, element in iparse:
        node = {}
        if element.tag == "way":
            input_by = {}
            for k,v in element.items():
                node['type'] =  element.tag
                if k == 'changeset':
                    node[k] = v
                if k == 'timestamp':
                    node[k] = v
                if k == "version":
                    node[k] = float(v)
                if k == "id":
                    node[k] = int(v)

                try:
                    if 'lat' or 'lon' in element.attrib:
                        node['pos'] = [float(element.attrib['lat']),float(element.attrib['lon'])]
                except KeyError:
                    pass

                if k == 'uid':
                    input_by[k] = v
                if k == 'user':
                    input_by[k] = v

                node['input_by'] = input_by


            address = {}
            for i in element.iter('tag'):
                if i.attrib['v'] == 'Jefferson Avenue':
                    print i
                if i.attrib['k'] == 'addr:city':
                    i.attrib['v'] = i.attrib['v'].title()
                # titles street names
                if i.attrib['k'] == 'addr:street':
                    i.attrib['v'] = i.attrib['v'].title()
                # turns street abbreviations into full name
                if i.attrib['k'] == 'addr:street':
                    search = street_type_re.findall(i.attrib['v'])
                    if search:
                        for items in search:
                            for k,v in mapping.items():
                                if items in k:
                                        # print items
                                    i.attrib['v'] = i.attrib['v'].replace(k,v)
                # # Manual fixes
                if 'Escarpado' in i.attrib['v']:
                    i.attrib['v'] = 'El Escarpado Avenue'

                if 'Las' in i.attrib['v']:
                    i.attrib['v'] = 'Alameda de las Pulgas'

                if 'Alameda' in i.attrib['v']:
                    i.attrib['v'] = 'Alameda de las Pulgas'

                t = lower_colon.findall(i.attrib['k'])
                if t:
                    if 'addr' in i.attrib['k']:
                        tester = i.attrib['k']
                        splitter = tester.split(':')[1]
                        address[splitter] = i.attrib['v']

                if t:
                    node['address'] = address

            my_data.append(node)
    return my_data

my_data = elements(iparse)
pprint.pprint(my_data)
