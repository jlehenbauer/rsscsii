import math

class Polygon:
    sides = None
    radius = None
    side_length = None
    height = None
    width = None
    perimeter = None
    area = None
    def __init__(self, sides=3, side_length=1):
        self.sides = sides
        self.side_length = side_length
    #this function uses self to find perimeter of polygon
    def get_perimeter(self):
        self.perimeter = self.sides * self.side_length
        return self.perimeter
    def get_area(self):
        apothem = self.side_length / (2 * math.tan(math.pi/self.sides))
        return apothem


