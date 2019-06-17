class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return 'x: %f, y: %f' % (self.x, self.y) 

    def __eq__(self, point):
        if(point):
            return (self.x == point.x and self.y == point.y)
        return False
