import json
from collections import defaultdict
from pprint import pprint

def process_locations_data(data):
    locations = defaultdict(int)
    for item in data['data']:
        location = item['relationships']['location']['data']['id']
        locations[location] += 1
    return locations

def process_locations_included(data):
    return_list = []
    for record in data['included']:
        id = record.get('id', None)
        name = record.get('attributes', {}).get('name', None)
        coord = record.get('attributes', {}).get('coord', None)
        return_list.append((id, name, coord))
    return return_list

with open('data-science.txt') as data_file:
    data = json.load(data_file)

locations = process_locations_data(data)
records = process_locations_included(data)

# combine the data for printing
for record in records:
    id, name, coord = record
    references = locations[id]
    print id, name, coord, references