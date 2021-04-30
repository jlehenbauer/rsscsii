from simpleimage import SimpleImage


def main():
    MIDDLE_EYE_BLUE = (193, 236, 241)
    NEW_BLUE = (0, 0, 255)
    """ 
    def change_color(r, g, b):
        pix.red = r
        pix.green = g
        pix.blue = b 
    def assign_blue(pix):
        return (pix.red == 193 and pix.green == 236 and pix.blue == 241)
    def assign_pcbrown(pix):
        return (pix.red == 64 and pix.green == 58 and pix.blue == 62)
    def assign_mnpink(pix):
        return (pix.red == 193 and pix.green == 236 and pix.blue == 241)
    def assign_flbrown(pix):
        return (pix.red == 199 and pix.green == 179 and pix.blue ==153) """
        
    image = SimpleImage('grumpycat.png')
    colors = []

    # for x in range(image.width):
    #     for y in range(image.height):
    #         pix = image.get_pixel(x, y)
    #         if (pix.red, pix.green, pix.blue) not in colors:
    #             colors.append((pix.red, pix.green, pix.blue))

    # print(colors)


    for x in range(image.width):
        for y in range(image.height):
            pix = image.get_pixel(x, y)
            if pix.blue > pix.red and pix.blue > pix.green:
                (pix.red, pix.green, pix.blue) = NEW_BLUE
            #main_eye_blue = assign_blue(pix)
            #pupil_center_brown = assign_pcbrown(pix)
            #main_nose_pink = assign_mnpink(pix)
            #face_light_brown = assign_flbrown(pix)
            #if main_eye_blue:
            #    change_color(255, 0, 0)
    image.show()

if __name__ == '__main__':
    main()