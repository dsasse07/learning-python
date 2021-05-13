from simpleimage import SimpleImage
from images import *

BRIGHT_PIXEL_THRESHOLD = 153

def main(pic):
    image = SimpleImage(pic)
    for pixel in image:
        pixel_average = get_pixel_average(pixel)
        if pixel_average > BRIGHT_PIXEL_THRESHOLD:
            convert_to_grayscale(pixel, pixel_average)
    # Apply the filter
    # TODO: your code here

    image.show()

def get_pixel_average(pixel):
    return (pixel.red + pixel.green + pixel.blue) // 3

def convert_to_grayscale(pixel, pixel_average):
    # Assigns a pixel value to be the average of its component colors
    pixel.red = pixel_average
    pixel.green = pixel_average
    pixel.blue = pixel_average

main(beach)