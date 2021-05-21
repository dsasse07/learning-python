import json
import os
dirname = os.path.dirname(__file__)

def file(r_path):
  return os.path.join(dirname, r_path)

def get_ages():
  with open(file('ages.json')) as age_file:
    ages = json.load(age_file)
    print('ages =', ages)
    print('ages["Chris"] =', ages['Chris'])

get_ages()

#Write JSON data

def write_ages():
  data={'Name':'Brahm','Age':24}
  with open(file('new_json.json'), 'w') as new_json:
    json.dump(data, new_json, indent=2)

write_ages()