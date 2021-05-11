from simpleimage import SimpleImage
from images import *

# MAIN = "./9-image-manipulation/stop.jpeg"
# BACKGROUND = "./9-image-manipulation/beach.jpeg"
MAIN = stop
BACKGROUND = beach
INTENSITY_THRESHOLD = 1.6

def red_screen(main_file, background_file):
  image = SimpleImage(main_file)
  back_image = SimpleImage(background_file)

  for pixel in image:
    average = (pixel.red + pixel.green + pixel.blue) // 3
    if pixel.red >= average * INTENSITY_THRESHOLD:
      # Replace this sufficiently green pixel with same pixel from background
      x = pixel.x
      y = pixel.y
      image.set_pixel(x, y, back_image.get_pixel(x,y))
  return image

red_screen(MAIN,BACKGROUND).show()