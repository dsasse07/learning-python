from simpleimage import SimpleImage
my_image = SimpleImage("./9-image-manipulation/test.jpeg")

'''
Image commands:
- image.width
- image.height

Pixel Commands:
- pixel.x, pixel.y
- pixel.red, pixel.green, pixel.blue

'''


def darker(file):
  image = get_file(file)
  for pixel in image:
    pixel.red //= 2
    pixel.blue //= 2
    pixel.green //= 2
  return image

def red_channel(image):
  image = get_file(image)
  for pixel in image:
    pixel.blue = 0
    pixel.green = 0
  return image

def grayscale(filename):
  '''
    Reads image from a filename.
    Converts to grayscale using luminosity
    Returns grayscale image
  '''
  image = get_file(filename)
  for pixel in (image):
    luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
    pixel.red = luminosity
    pixel.blue = luminosity
    pixel.green = luminosity
  return image

def compute_luminosity(red, green, blue):
  '''
    Uses NTSC formula to convert color values into grayscale
  '''
  return (0.299 * red) + (0.587 * green) + (0.114 * blue)

def get_file(filename):
  if type(filename) is str:
    image = SimpleImage(filename)
  else:
    image = filename
  return image

my_image.show()
grayscale("./9-image-manipulation/test2.jpeg").show()
grayscale(my_image).show()
red_channel(my_image).show()
