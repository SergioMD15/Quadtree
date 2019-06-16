from Quad import Quad
from Point import Point


class Tree:
    def __init__(self, size):
        self.size = size
        self.quad = None

    def insert(self, x, y):
        point = Point(x, y)
        if(x > self.size or y > self.size):
            print('The point is out of the limits')
        else:
            if(not self.quad):
                self.quad = Quad(point, self.size / 2, self.size / 2)
            else:
                self.quad.insert(point)

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
            value = self.quad.find_quad(Point(x, y))
            return value
