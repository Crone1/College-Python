
class Shape(object):

    def __init__(self, points):
        self.points = points

    def sides(self):
        org = point_one = self.points[0]
        sides = []

        for point_two in self.points[1:]:
            sides.append(abs(point_one.distance(point_two)))
            point_one = point_two

        sides.append(abs(point_one.distance(org)))
        return sides

    def perimeter(self):
        perimeter = 0
        for side in self.sides():
            perimeter = perimeter + side

        return perimeter


class Point(Shape):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        x = (self.x - other.x)**2
        y = (self.y - other.y)**2
        return (x + y)**0.5


class Triangle(Shape):

    def area(self):
        a = self.sides()[0]
        b = self.sides()[1]
        c = self.sides()[2]
        s = (a + b + c) / 2
        return (s * (s - a) * (s - b) * (s - c))**(1 / 2)


class Square(Shape):

    def area(self):
        return (self.sides()[0])**2
