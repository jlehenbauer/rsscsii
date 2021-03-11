from polygons import Polygon

def main():
    sides = int(input("how many sides do you want? "))
    side_length = int(input("what do you want the length of the sides to be? "))
    poly=Polygon(sides, side_length)
    print(poly.get_area())

    print("Your polygon's apothem is " + str(poly.apothem))
    print("Your polygon's perimeter is " + str(poly.perimeter))
    print("Your polygon's area is " + str(poly.area))
if __name__ == "__main__":
    main()
