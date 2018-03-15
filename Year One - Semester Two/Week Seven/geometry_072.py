
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, p2):
        new_x = int(p2.x) - int(self.x)
        new_y = int(p2.y) - int(self.y)
        return ((new_y)**2 + (new_x)**2)**(1 / 2)

    def __str__(self):
        return '({:.1f}, {:.1f})'.format(self.x, self.y)


class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint(self):
        x = (self.p1.x + self.p2.x) / 2
        y = (self.p1.y + self.p2.y) / 2
        return '({:.1f}, {:.1f})'.format(x, y)

    def length(self):
        return self.p2 - self.p1


class Circle(object):

    def __init__(self, center, radius):
        self.r = radius
        self.c = center

    def overlaps(self, cent):
        return ((cent.c.x - self.c.x)**2) + ((cent.c.y - self.c.y)**2) < ((cent.r + self.r)**2)
