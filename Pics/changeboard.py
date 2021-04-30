from simpleimage import SimpleImage

def main():
    image = SimpleImage('standardboard.png')
    for x in range(image.width):
        for y in range(image.height):
            pix = image.get_pixel(x, y)
            if pix.red == 87 and pix.blue == 82 and pix.green == 84:
                pix.red = 255
                pix.green = 225
                pix.blue = 255
    image.show()

if __name__ == '__main__':
    main()