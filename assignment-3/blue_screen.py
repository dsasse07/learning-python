"""
File: bluescreen.py
----------------
Not part of the assignment. This was a lecture demo!
This is a fun algorithm to implement. It is not in the
assignment, but feel free to implement it as an extension.
Put the smaller foreground picture into the background.
Do not include any pixels that are sufficiently blue.
"""

from simpleimage import SimpleImage


def main():
    foreground = SimpleImage('assignment-3/images/tiefighter.jpg')
    background = SimpleImage('assignment-3/images/quad.jpg')
    # TODO: your code here
    for i in range(foreground.width):
        for j in range(foreground.height):
            fg_pixel = foreground.get_pixel(i,j)
            average = sum([fg_pixel.red, fg_pixel.blue, fg_pixel.green]) / 3
            if fg_pixel.blue < average * 1.6 :
                background.set_pixel(i,j,fg_pixel)
    background.show()


if __name__ == '__main__':
    main()