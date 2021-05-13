from simpleimage import SimpleImage
from images import beach

def main(pic):
    image = SimpleImage(pic)
    image.show()
    trimmed_img = trim_crop_image(image, 300)
    trimmed_img.show()


def trim_crop_image(original_img, trim_size):
    """
    This function returns a new SimpleImage which is a trimmed and
    cropped version of the original image by shaving trim_sz pixels
    from each side (top, left, bottom, right) of the image. You may
    assume trim_sz is less than half the width of the image.

    Inputs:
        - original_img: The original image to process
        - trim_size: The number of pixels to shave from each side of the original image

    Returns:
        A new SimpleImage with trim_sz pixels shaved off each
        side of the original image
    """
    new_x_start = trim_size
    new_x_end = original_img.width - trim_size
    new_y_start = trim_size
    new_y_end = original_img.height - trim_size

    new_width = new_x_end - new_x_start
    new_height = new_y_end - new_y_start

    cropped_image = SimpleImage.blank(new_width, new_height)
    
    for i in range(new_x_start, new_x_end):
        for j in range(new_y_start, new_y_end):
            original_pixel = original_img.get_pixel(i,j)
            cropped_image.set_pixel( (i - trim_size), (j - trim_size), original_pixel)
    return cropped_image

main(beach)