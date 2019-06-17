from Point import Point

class Quad:

    def __init__(self, point, size, half_x, half_y):
        self.children = {'NE': None,
                         'SE': None,
                         'SW': None,
                         'NW': None }
        self.point = point
        self.half_x = half_x
        self.half_y = half_y
        self.size = size
        self.leaf = True

    def insert(self, point):
        """
        Adds a new point to the Quadtree.
        
        If it fits in this quad, is inserted at this level,
        otherwise we go a level down selecting the most accurate
        cardinality for the given point.

        Parameters
        ----------
        point : Point
            Coordinates (x,y) of the point to be inserted in the tree.

        Returns
        -------
        Point
            Middle point (x,y) of the quad the point belongs to.
        """

        if(self.is_leaf()):
            self.subdivide()
        key = self.get_cardinality(point)
        size = self.get_new_halfs(key)
        if(self.children[key]):
            return self.children[key].insert(point)
        else:
            self.children[key] = Quad(point, self.size / 2, size.x, size.y)
            return size

    def subdivide(self):
        pos = self.get_cardinality(self.point)
        size = self.get_new_halfs(pos)
        self.children[pos] = Quad(self.point, self.size / 2, size.x, size.y)
        self.leaf = False
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
        pos = self.get_cardinality(point)
        if(self.children[pos]):
            if(self.children[pos].is_leaf()):
                self.children[pos] = None
                return True
            else:
                deletion = self.children[pos].delete(point)
                keys = [i for i in self.children.keys() if i]
                if(deletion and len(keys) == 1):
                    self.point = self.children[keys[0]].point
                    self.children[keys[0]] = None
                    self.leaf = True
                    return deletion
                else:
                    return deletion

        else:
            return False

    def is_leaf(self):
        return self.leaf
