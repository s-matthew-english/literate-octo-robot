import json
import requests
from collections import defaultdict
from pprint import pprint

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

# open up the output of 'data-processing.py'
with open('job-numbers-by-location.txt') as data_file:

    # print the output to a file
    with open('phase_ii_output.txt', 'w') as output_file_:
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
                        # print("code: " + country_code + ", jobs: " + number_of_jobs)
                        output_file_.write("code: " + country_code + ", jobs: " + number_of_jobs)
    output_file_.close()





