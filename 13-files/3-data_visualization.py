from simpleimage import SimpleImage
import os
dirname = os.path.dirname(__file__)

def file(r_path):
  return os.path.join(dirname, r_path)


''' 
  Lets map city & population data for the world.
  If we imagine a map as a giant picture, we could think of
  lat/long as pixels in the photo.

  There are numerous libraries that will do this already
'''

COUNTRY_DIRECTORY = 'countries/'

'''
  Dimensions of the final visualization. Change these if the 
  image is too large for your screen
'''
VISUALIZATION_WIDTH = 1920
VISUALIZATION_HEIGHT = 1080

'''
Setting the 'boundaries' for the visualization. By default, the 
visualization holds the entire world. If you want to zoom in on a 
specific country, you can find the corresponding latitudes and longitudes 
here: https://gist.github.com/graydon/11198540
'''
MIN_LONGITUDE = -180
MAX_LONGITUDE = 180
MIN_LATITUDE = -90
MAX_LATITUDE = 90

def main():
  # Create Blank Map
  visualization = SimpleImage.blank(VISUALIZATION_WIDTH, VISUALIZATION_HEIGHT)
  # Get List of countries to be mapped
  countries = get_countries()
  for country in countries:
    country_filename = file(COUNTRY_DIRECTORY + country + '.csv')
    plot_country(visualization, country_filename)
  visualization.show()

def plot_country(visualization, country_filename):
  with open(country_filename) as country_file:
    next(country_file) # Skip the table headers
    for city in country_file:
      data = city.strip().split(',')
      latitude = float(data[1])
      longitude = float(data[2])
      plot_one_city(visualization, latitude, longitude)

def get_countries():
  list = []
  while True:
    country = input('Enter a country, or "all". Press Enter to finish: ')
    if country == '': break
    elif country == 'all':
      # Read each file in directory as array, return eachname prior to .extension
      return [filename.split(".")[0] for filename in os.listdir(file(COUNTRY_DIRECTORY))]
    else:
      list.append(country.strip())
  return list

def plot_one_city(visualization, latitude, longitude):
  # Convert Lat/Long to pixels
  x = longitude_to_x(longitude)
  y = latitude_to_x(latitude)
  # If valid, plot it
  if 0 < x < VISUALIZATION_WIDTH and 0 < y < VISUALIZATION_HEIGHT:
    plot_pixel(visualization, x, y)

def longitude_to_x(longitude):
  '''
      x        long - Min
  ________  =  ___________
    width      Max - Min
  '''
  return VISUALIZATION_WIDTH * (longitude - MIN_LONGITUDE) / (MAX_LONGITUDE - MIN_LONGITUDE)

def latitude_to_x(latitude):
  return VISUALIZATION_HEIGHT * (1.0 - (latitude - MIN_LATITUDE) / (MAX_LATITUDE - MIN_LATITUDE))

def plot_pixel(visualization, x, y):
  pixel = visualization.get_pixel(x,y)
  pixel.green = 0
  pixel.red = 0

main()

