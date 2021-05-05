"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'greenland-fire.png'
INTENSITY_THRESHOLD = 1.15

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)

    for px in image:
        
        #TODO: Calculate average of green, blue, and red and mutiply by INTENSITY_THRESHOLD
        my_average = ((px.red + px.green + px.blue)/3) 
        average_int = my_average * INTENSITY_THRESHOLD
        #TODO: If a pixel's red is higher than this average, set it completely red, otherwise, set it to the average
        if px.red > my_average:
            px.red = 255
            px.blue = 0
            px.green = 0
        else:
            px.red = INTENSITY_THRESHOLD
            px.blue = INTENSITY_THRESHOLD
            px.green = INTENSITY_THRESHOLD
    return image

def main():
    # Get file and load image
    filename = get_file()
    image = SimpleImage(filename)

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()

    
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
