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
            print('There are no points yet')
        else:
            value = self.quad.find_quad(Point(x, y))
            print('x: %.2f;y: %.2f' % (value.x, value.y))
