#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
from pymongo import MongoClient
from collections import defaultdict
import json


osmfile = '/Users/tonynguyen/Desktop/Codes/Udacity/Data_Analyst/Project_3/Project_3/sample.osm'
parse = iparse = ET.iterparse(osmfile, events=("start",))

# typical street names that are expected
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road",
            "Trail", "Parkway", "Commons"]

# typical street abbreviations
mapping = {"St.": "Street",
           "St": "Street",
           "Rd": "Road",
           "Rd.": "Road",
           "Ave": "Avenue",
           "Ave.": "Avenue"}

# some regular expression searches to look for anomalies (taken from the quiz)
lower = re.compile(r'^([a-z]|_)*$')  # finds all lower case keys
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')  # finds all keys with a colon
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]') # finds any problem characters
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE) # find the street types
re_post =  re.compile(r'^\d{5}$') #finds post codes

# dictionaries and list to store my data
odd_streets = []
cities = []
city_count = {} # stores the number of cities found in the data
odd_streets_count = {} # stores number of odd streets (steets not found in expected)

# stores the odd characters that was found during the regular expressions queries
odd_keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}

def stats(iparse):
    for event, element in iparse:
        if element.tag == "node" or element.tag == "way":

            for i in element.iter('tag'):
                """
                city total, use city_count
                """
                if 'addr:city' in i.attrib['k']:
                    cities.append(i.attrib['v'])
                    for q in set(cities):
                        city_count[q] = cities.count(q)

                """
                a count of all the streets to find any irregularity,
                use odd_streets_count
                """
                if i.attrib['k'] == 'addr:street':
                    street_end = street_type_re.search(i.attrib['v'])
                    odd_streets.append(street_end.group())
                    for q in set(odd_streets):
                        odd_streets_count[q] = odd_streets.count(q)


                """
                This looks for any odd characters, and prints out a count in the
                keys dictionary. we can also print the elements. Just uncomment
                print statment
                """

                if lower.search(i.attrib['k']):
                    odd_keys["lower"] += 1
                    # print i.attrib

                elif lower_colon.search(i.attrib['k']):
                    odd_keys['lower_colon'] += 1
                    # print i.attrib

                elif problemchars.search(i.attrib['k']):
                    odd_keys['problemchars'] += 1
                    # print i.attrib

                else:
                    odd_keys['other'] += 1
                    # print i.attrib


def elements(iparse):
    """
    extracts data from the OSM and stores it into my_data
    """
    my_data = []
    for key, element in iparse:
        node = {}
        if element.tag == "node" or element.tag == "way":
            input_by = {}
            for k,v in element.items():
                node['type'] = element.tag
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
            details = {}
            for i in element.iter('tag'):
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

                #post code fixes
                #post code fixes
                if i.attrib['k'] == "addr:postcode":
                    postal_split = i.attrib['v'].split('-')[0]
                    tester = (re_post.findall(postal_split))
                    for post in tester:
                        i.attrib['v'] = post


                # Manual fixes
                if 'Escarpado' in i.attrib['v']:
                    i.attrib['v'] = 'El Escarpado Avenue'

                if 'Las' in i.attrib['v']:
                    i.attrib['v'] = 'Alameda de las Pulgas'

                if 'Alameda' in i.attrib['v']:
                    i.attrib['v'] = 'Alameda de las Pulgas'


                if 'addr' not in i.attrib['k']:
                    if ':' in i.attrib['k']:
                        split = i.attrib['k'].split(':')
                        details[split[1]] = i.attrib['v']

                    if ':' not in i.attrib['k']:
                        details[i.attrib['k']] =i.attrib['v']

                t = lower_colon.findall(i.attrib['k'])
                if t:
                    if 'addr' in i.attrib['k']:
                        tester = i.attrib['k']
                        splitter = tester.split(':')[1]
                        address[splitter] = i.attrib['v']

                if t:
                    node['address'] = address
                    node['details'] = details

            my_data.append(node)
    return my_data

def export_json(my_data):
    """
    imports my_data into JSOn file
    """
    with open('sample.json', 'w') as outfile:
        json.dump(my_data, outfile)

export_json(elements(iparse))

#The code below was used to extract all the data that contained a certian certian,
#but ater evaluating that data, there was an insufficient amount of data needed.
#The idea was scrapped.
#
# mpk = root.iterfind(".//tag[@v='Menlo Park']..") #find all values where v = palo alto, and find the parent
#
# for i in mpk: #for every parent
#     parent = i.attrib #print parent (ways)
#     for t in i.iterfind('./'): #finds child (tags)
#         child = t.attrib
