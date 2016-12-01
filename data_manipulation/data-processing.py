import json
from collections import defaultdict
from pprint import pprint


def process_locations_data(data):
    # processes the 'data' block
    locations = defaultdict(int)
    for item in data['data']:
        location = item['relationships']['location']['data']['id']
        locations[location] += 1
    return locations


def process_locations_included(data):
    # processes the 'included' block
    return_list = []
    for record in data['included']:
        id = record.get('id', None)
        name = record.get('attributes', {}).get('name', None)
        coord = record.get('attributes', {}).get('coord', None)
        return_list.append((id, name, coord))
    return return_list    # return list of tuples


# load the data from file once
with open('data-science.txt') as data_file:
    data = json.load(data_file)


# use the two functions on same data
locations = process_locations_data(data)
records = process_locations_included(data)


# output list to collect lines
output = []


# combine the data for printing
for record in records:
    id, name, coord = record
    references = locations[id]   # lookup the references in the dict
    line = str(id) + "  " + str(name) + "   " + str(coord) + "  " + str(references) + "\n"
    if line not in output:
        output.append(line)


# print the output to a file
with open('MASTER-CHOPPER-OUTPUT.txt', 'w') as file_:
    for l in output:
        if not ("None") in l:
            file_.write(l)
file_.close()




