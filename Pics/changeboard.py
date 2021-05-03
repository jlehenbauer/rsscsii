from simpleimage import SimpleImage

def main():
    image = SimpleImage('standardboard.png')
    for x in range(image.width):
        for y in range(image.height):
            pix = image.get_pixel(x, y)
            if 60 < pix.red < 90 and 60 < pix.green < 90 and 60 < pix.red < 90:
                pix.red = pix.red * 2
                pix.blue = pix.blue * 2
                pix.green = 0
    
    image.show()

if __name__ == '__main__':
    main()