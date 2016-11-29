import json
from collections import defaultdict
from pprint import pprint

with open('prettyPrint.txt') as data_file:
    data = json.load(data_file)

locations = defaultdict(int)

for item in data['data']:
    location = item['relationships']['location']['data']['id']
    locations[location] += 1

pprint(locations)




# print each id that corresponds to a single location
#
# for item in data['data']:
#     location = item['relationships']['location']['data']['id']
#     locations[location].append(item['id'])
#
# pprint(locations)







# Get the location data and id
#
# for item in data["data"]:
#     print(item['id'], item['relationships']['location'])


# This prints the job title, just some practice
#
# for item in data["data"]:
#     for job in item["attributes"]["title"].splitlines():
#         print( job )





#######################################################
#   old file
#######################################################
# import json
# from pprint import pprint
#
# with open('data.json') as data_file:
#     data = json.load(data_file)
#
#
#
#     for item in data["data"]:
#         # count up by location
#         for item['relationships']['location']:
#
#         item['id']
#
########################################################
