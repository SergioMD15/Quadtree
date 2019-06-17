from Point import Point

class Quad:

    def __init__(self, point, half_x, half_y):
        self.children = {'NE': None,
                         'SE': None,
                         'SW': None,
                         'NW': None }
        self.point = point
        self.half_x = half_x
        self.half_y = half_y
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
        key, size = self.get_cardinality(point)
        if(self.children[key]):
            return self.children[key].insert(point)
        else:
            self.children[key] = Quad(point, size.x, size.y)
            return size

    def subdivide(self):
        pos, size = self.get_cardinality(self.point)
        self.children[pos] = Quad(self.point, size.x, size.y)
        self.leaf = False
        self.point = None

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
        elif (pos == 'SW'):
            return Point(self.half_x - self.half_x/2, self.half_y - self.half_y / 2)
        else:
            return None

    # def delete(self, point):
    #     cardinality, size = self.get_cardinality(point)
    #     if(self.children[key] == )

    def is_leaf(self):
        return self.leaf
