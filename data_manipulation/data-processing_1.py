import json
import requests
from collections import defaultdict
from pprint import pprint

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

# open up the output of 'data-processing.py'
with open('job-numbers-by-location.txt') as data_file:

    for line in data_file:
        identifier, name, coords, number_of_jobs = line.split("|")
        coords = coords[1:-1]
        lat, lng = coords.split(",")
        # print("lat: " + lat, "lng: " + lng)
        response = requests.get("http://api.geonames.org/countrySubdivisionJSON?lat="+lat+"&lng="+lng+"&username=s.matthew.english").json()


        codes = response.get('codes', [])
        for code in codes:
            if code.get('type') == 'ISO3166-2':
                country_code = '{}-{}'.format(response.get('countryCode', 'UNKNOWN'), code.get('code', 'UNKNOWN'))
                if not hasNumbers( country_code ):
                    print("code: " + country_code + ", jobs: " + number_of_jobs)






        # did = response.get('countryCode', None)
        # name = response.get('codes', {}).get('name', {})
        # # coord = response.get('attributes', {}).get('coord', None)
        # print(name)


        # print(json.dumps(response["codes"]["ISO3166-2"]))





        # coord = response.get('codes', {}).get('type', {}).get('ISO3166-2', None)
        # print(coord)





        # try:
        #     # print(response["codes"])
        #     print(json.dumps(response["countryCode"]))
        # except:
        #     pass


