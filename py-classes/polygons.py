import math

class Polygon:
    
    radius = None
    height = None
    width = None
    
    def __init__(self, sides=3, side_length=1):
        self.sides = sides
        self.side_length = side_length
        self.perimeter = self.sides * self.side_length
        self.apothem = self.side_length / (2 * math.tan(math.pi/self.sides))
        self.area = 1/2*(self.apothem * self.perimeter)
    #this function uses self to find the area of our polygon
    def get_area(self):
        return self.area

class Triangle(Polygon):
    def __init__(self, side_length=1):
        super().__init__(3, side_length)
        self.height = self.apothem * 3
        self.width = self.side_length
class Hexagon(Polygon):
    def __init__(self, side_length=1):
        super().__init__(6, side_length)
        self.height = self.apothem * 3
        self.width = self.side_length
        self.long_diagonal = self.side_length * 2
        self.short_diagonal = math.root(3) * self.side_length
class Heptagon(Polygon):
    def __init__(self, side_length=1):
        super().__init__(7, side_length)
        self.height = self.side_length/(2 * math.tan((math.pi/2)/self.sides))
        self.width = self.side_length
        self.long_diagonal = self.side_length / (2 * math.sin((math.pi/2)/self.sides))
        self.short_diagonal = 2 * self.side_length * math.cos(math.pi/self.sides)
class Octagon(Polygon):
    def __init__(self, side_length=1):
        super().__init__(8, side_length)
        self.height = self.apothem * 3
        self.width = self.side_length
        self.long_diagonal = self.side_length * math.root(4 + 2 * math.root(2)) 
        self.short_diagonal = math.root(3) * self.side_length