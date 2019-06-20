from Point import Point


class Quad:

    def __init__(self, point, size, half_x, half_y):
        self.children = {'NE': None,
                         'SE': None,
                         'SW': None,
                         'NW': None}
        self.point = point
        self.half_x = half_x
        self.half_y = half_y
        self.size = size
        self.removable = False

    def insert(self, point):
        if(self.point):
            self.subdivide()
        key = self.get_cardinality(point)
        size = self.get_new_halfs(key)
        if(self.children[key]):
            self.children[key].insert(point)
        else:
            self.children[key] = Quad(point, self.size / 2, size.x, size.y)

    def get_used_quads(self):
        return [i for i in self.children.keys() if self.children[i]]

    def subdivide(self):
        pos = self.get_cardinality(self.point)
        size = self.get_new_halfs(pos)
        self.children[pos] = Quad(self.point, self.size / 2, size.x, size.y)
        self.point = None

    def find_quad(self, point):
        if(point == self.point):
            return (Point(self.half_x, self.half_y))
        else:
            pos = self.get_cardinality(point)
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
        return pos

    def get_new_halfs(self, pos):
        inc = self.size / 4
        if (pos == 'NE'):
            return Point(self.half_x + inc, self.half_y + inc)
        elif (pos == 'SE'):
            return Point(self.half_x + inc, abs(self.half_y - inc))
        elif (pos == 'NW'):
            return Point(abs(self.half_x - inc), self.half_y + inc)
        elif (pos == 'SW'):
            return Point(abs(self.half_x - inc), abs(self.half_y - inc))
        else:
            return None

    def delete(self, point):
        if(self.point == point):
            self.point = None
            self.removable = True
            return True
        else:
            pos = self.get_cardinality(point)
            if(pos and self.children[pos]):
                deleted = self.children[pos].delete(point)
                if(deleted):
                    if (self.children[pos].removable):
                        self.children[pos] = None
                    keys = self.get_used_quads()
                    if(len(keys) == 1 and len(self.children[keys[0]].get_used_quads()) == 0):
                        self.point = self.children[keys[0]].point
                        self.children[keys[0]] = None
                return deleted
            return False
