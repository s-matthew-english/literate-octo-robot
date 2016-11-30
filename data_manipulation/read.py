import json
from collections import defaultdict
from pprint import pprint

with open('data-science.txt') as data_file:
    data = json.load(data_file)

locations = defaultdict(int)

for record in data['included']:
    id = record.get('id', None)
    name = record.get('attributes', {}).get('name', None)
    coord = record.get('attributes', {}).get('coord', None)
    print(id, name, coord)



#     location = item['included']['id']['coord']
#     locations[location].append(item['coord'])
#  .get( ['coord'] )
# pprint(locations)

