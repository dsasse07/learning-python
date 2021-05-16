"""
This program generates the Warhol effect based on the original image.
"""

from simpleimage import SimpleImage
import random

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    patches = []
    create_patches(patches)
    stitch_patches(patches, final_image)
    final_image.show()

def create_patches(patches):
    for i in range(N_COLS * N_ROWS):
        patch = make_recolored_patch(random_scale(1.4), random_scale(1.4), random_scale(1.4))
        patches.append(patch)

def stitch_patches(patches, final_image):
    for i in range(N_ROWS):
        for j in range (N_COLS):
            patch = patches.pop()
            insert_patch(patch, final_image, i,j)

def insert_patch(patch, final_image, row, col):
    for x in range(patch.width):
        for y in range(patch.height):
            pixel = patch.get_pixel(x,y)
            final_image.set_pixel(x + (PATCH_SIZE * col), y + (PATCH_SIZE * row), pixel)

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
    return patch

def random_scale(max):
    '''
        Returns a random float between 0 and max
    '''
    return random.random() * 1000 % max

if __name__ == '__main__':
    main()