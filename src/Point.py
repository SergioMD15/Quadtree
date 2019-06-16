class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print('x: %.2f, y: %.2f' % (self.x, self.y))

    def __eq__(self, point):
        return (self.x == point.x and self.y == point.y)
