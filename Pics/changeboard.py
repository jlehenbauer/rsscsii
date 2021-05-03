from simpleimage import SimpleImage

def main():
    image = SimpleImage('standardboard.png')
    for x in range(image.width):
        for y in range(image.height):
            pix = image.get_pixel(x, y)
<<<<<<< HEAD
            if 60 < pix.red < 90 and 60 < pix.green < 90 and 60 < pix.red < 90:
                pix.red = pix.red * 2
                pix.blue = pix.blue * 2
                pix.green = 0
    
=======
            if pix.red == 87 and pix.blue == 82 and pix.green == 84:
                pix.red = 255
                pix.green = 225
                pix.blue = 255
>>>>>>> 685bd18a9f4bf885f405984987e48e415f2000fe
    image.show()

if __name__ == '__main__':
    main()