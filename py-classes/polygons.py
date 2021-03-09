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
    def get_area(self):
        self.perimeter = self.sides * self.side_length
        #return self.perimeter
        self.apothem = apothem = self.side_length / (2 * math.tan(math.pi/self.sides))
        #return self.apothem
        self.area = 1/2*(self.apothem * self.perimeter)
        return self.area

