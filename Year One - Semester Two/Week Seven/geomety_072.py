
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p2):
        new_x = int(p2.x) - int(self.x)
        new_y = int(p2.y) - int(self.y)
        return ((new_y)**2 + (new_x)**2)**(1 / 2)

    def __str__():
        return '({:.1f}, {:.1f})'.format(self.x, self.y)


class Segment(object):

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def midpoint():
        self.p2 - self - p1

    def length():
        return self.p2 - self.p1


class Cicle(object):

    def __init__(self, radius, center):

    def overlap(self, cent):
        return ((cent.c1 - self.c1)**2) + ((cent.c2 - self.c2)**2) < ((cent.r + self.r)**2)
