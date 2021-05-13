from simpleimage import SimpleImage
from images import stop

def main(pic):
    image = SimpleImage(pic)
    bordered_img = add_border(image, 10)
    bordered_img.show()


def add_border(original_img, border_size):
    """
    This function returns a new SimpleImage which is the same as
    original image except with a black border added around it. The
    border should be border_size many pixels thick.

    Inputs:
        - original_img: The original image to process
        - border_size: The thickness of the border to add around the image

    Returns:
        A new SimpleImage with the border added around original image
    """
    new_width = original_img.width + (2 * border_size)
    new_height = original_img.height + (2 * border_size)
    new_image = SimpleImage.blank( new_width, new_height )
    border_pixel = original_img.get_pixel(1,1)
    border_pixel.red = 0
    border_pixel.blue = 0
    border_pixel.green = 0

    for i in range(new_width):
      for j in range(new_height):
        if i <= border_size or i >= new_width - border_size: 
          new_image.set_pixel(i,j,border_pixel)
        elif j <= border_size or j >= new_height - border_size: 
          new_image.set_pixel(i,j,border_pixel)
        else: 
          pass
          orig_pixel = original_img.get_pixel(i - border_size, j - border_size)
          new_image.set_pixel(i,j,orig_pixel)
    return new_image

main(stop)

