from Quad import Quad
from Point import Point


class Tree:
    def __init__(self, size):
        self.size = size
        self.quad = None
        self.points = []

    def insert(self, x, y):
        point = Point(x, y)
        if(x > self.size or y > self.size):
            print('The point is out of the limits')
        else:
            if(not self.quad):
                half = self.size / 2
                self.quad = Quad(point, half, half)
                self.points.append(point)
            else:
                result = self.quad.insert(point)
                self.points.append(point)

    def find(self, x, y):
        if(self.quad == None):
            return None
        else:
            value = self.quad.find_quad(Point(x, y))
            return value

    def delete(self, x, y):
        point = Point(x,y)
        if(self.quad == None):
            return None
        else:
            return self.quad.delete(Point(x, y))

    def print_points(self):
        for p in self.points:
            print(self.find(p.x, p.y))
