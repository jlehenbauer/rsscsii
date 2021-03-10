from polygons import Polygon

def main():
    poly=Polygon(4, 3)
    print(poly.get_area())
    sides = int(input("how many sides do you want?"))
if __name__ == "__main__":
    main()