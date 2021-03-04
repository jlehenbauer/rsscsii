class Polygon:
    sides = None
    radius = None
    side_length = None
    height = None
    width = None
    perimiter = None
    area = None
    def __init__(self, sides=3, side_length=1):
        self.sides = sides
        self.side_length = side_length
    def get_perimiter(self):
        perimiter = self.sides * self.side_length