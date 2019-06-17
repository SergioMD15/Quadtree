from Quad import Quad
from Point import Point


class Tree:
    def __init__(self, size):
        self.size = size
        self.half_x = size / 2
        self.half_y = self.half_x
        self.points = []
        self.quad = None

    def insert(self, x, y):
        point = Point(x, y)
        if((x > self.size or y > self.size) or point in self.points):
            print('The point is not valid')
            return
        else:
            if(not self.quad):
                self.quad = Quad(point, self.size, self.half_x, self.half_y)
            else:
                self.quad.insert(point)
            self.points.append(point)

    def find(self, x, y):
        if(self.quad == None):
            return None
        else:
            value = self.quad.find_quad(Point(x, y))
            return value

    def delete(self, x, y):
        point = Point(x,y)
        if(not self.quad.delete(point)):
            print('The point was not found')
        else:
            self.points.remove(point)
            

    def print_points(self):
        for p in self.points:
            print('Point: (%d, %d): (%s)' % (p.x, p.y, str(self.find(p.x, p.y))))
