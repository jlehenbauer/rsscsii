import math

class Polygon:
    
    radius = None
    height = Nonecs
    width = None
    
    def __init__(self, sides=3, side_length=1):
        self.sides = sides
        self.side_length = side_length
        self.perimeter = self.sides * self.side_length
        self.apothem = apothem = self.side_length / (2 * math.tan(math.pi/self.sides))
        self.area = 1/2*(self.apothem * self.perimeter)
    #this function uses self to find perimeter of polygon
    def get_area(self):
        return self.area

