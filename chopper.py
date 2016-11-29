import json
from pprint import pprint

with open('data.json') as data_file:
    data = json.load(data_file)


    for item in data["data"]:
        print(item['id'], item['relationships']['location'])



# This prints the job title, just some practice
#
# for item in data["data"]:
#     for job in item["attributes"]["title"].splitlines():
#         print( job )


