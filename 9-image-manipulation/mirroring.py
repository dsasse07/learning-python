from simpleimage import SimpleImage
from images import stop

def mirror(filename):
  image = SimpleImage(filename)
  width = image.width
  height = image.height
  result = SimpleImage.blank(width * 2, height)

  for y in range(height):
    for x in range(width):
      pixel = image.get_pixel(x,y)
      result.set_pixel(x,y,pixel)
      result.set_pixel((width * 2) - (x + 1), y, pixel)

  return result

mirror(stop).show()