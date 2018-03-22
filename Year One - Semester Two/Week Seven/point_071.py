
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = '-' + str(self.x)
        self.y = '-' + str(self.y)

    def distance(self, p2):
        new_x = int(p2.x) - int(self.x)
        new_y = int(p2.y) - int(self.y)
        return ((new_y)**2 + (new_x)**2)**(1 / 2)
