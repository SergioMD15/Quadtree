from Point import Point

class Quad:

    def __init__(self, point, half_x, half_y):
        self.children = {'NE': None,
                         'NW': None,
                         'SW': None,
                         'SE': None, }
        self.point = point
        self.half_x = half_x
        self.half_y = half_y
        self.leaf = True

    def insert(self, point):
        if(self.leaf):
            self.subdivide()
        key, size = self.get_cardinality(point)
        if(self.children[key]):
            self.children[key].insert(point)
        else:
            self.children[key] = Quad(point, size.x, size.y)

    def subdivide(self):
        pos, size = self.get_cardinality(self.point)
        self.children[pos] = Quad(self.point, size.x, size.y)
        self.leaf = False

    def is_empty(self):
        return len([i for i in self.children.values() if i != None]) == 0

    def find_quad(self, point):
        if(point == self.point):
            return (Point(self.half_x, self.half_y))
        else:
            pos, halfs = self.get_cardinality(point)
            if(self.children[pos]):
                return self.children[pos].find_quad(point)
            return None

    def get_cardinality(self, point):
        pos = None
        if(point.x >= self.half_x and point.y >= self.half_y):
            pos = 'NE'
        elif(point.x >= self.half_x and point.y < self.half_y):
            pos = 'SE'
        elif(point.x < self.half_x and point.y >= self.half_y):
            pos = 'NW'
        elif(point.x < self.half_x and point.y < self.half_y):
            pos = 'SW'
        return pos, self.get_new_halfs(pos)

    def get_new_halfs(self, pos):
        if (pos == 'NE'):
            return Point(self.half_x + self.half_x/2, self.half_y + self.half_y / 2)
        elif (pos == 'SE'):
            return Point(self.half_x + self.half_x/2, self.half_y - self.half_y / 2)
        elif (pos == 'NW'):
            return Point(self.half_x - self.half_x/2, self.half_y + self.half_y / 2)
        else:
            return Point(self.half_x - self.half_x/2, self.half_y - self.half_y / 2)
