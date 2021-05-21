import os
dirname = os.path.dirname(__file__)

def file(r_path):
  return os.path.join(dirname, r_path)

# User CSV library for CSV files
import csv
def plot_country():
  with open(file(USA.csv)) as country_file:
    next(country_file) #Skip Header
    reader = csv.reader(country_file)
    # Reader from library does the splitting and stripping automatically
    for line in reader:
      lat = float(line[1])
      long = float(line[2])

# Dict Reader uses the first row of CSV file to get headers and make them into keys!
def plot_country():
  with open(file(USA.csv)) as country_file:
    reader = csv.DictReader(country_file)
    # Reader from library does the splitting and stripping automatically
    for line in reader:
      lat = float(line['Latitude'])
      long = float(line['Longitude'])


# Writing CSV
def write_data_from_list():
  with open(file('data.csv'), 'w') as new_file:
    writer = csv.writer(new_file)
    writer.writerow(['x','y'])
    writer.writerows([
      [1,2],
      [2,4],
      [4,6]
    ])

def write_data_from_dict():
  with open(file('data.csv'), 'w') as new_file:
    columns = ['x','y']
    writer = csv.DictWriter(new_file)
    writer.writeheader(fieldnames=columns)
    writer.writerow({'x':1, 'y':2})
    writer.writerows([
      {'x':2,'y':4},
      {'x':4,'y':6}
    ])


'''
  Why use CSV files?
  - Good for tables & tabular data
  - Understood by Google Sheets or Excel
'''