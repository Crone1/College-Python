
class Score(object):

    def score_to_points(self):
        return (self.goals * 3) + self.points

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def __eq__(self, other):
        return self.score_to_points() == other.score_to_points()

    def __gt__(self, other):
        return self.score_to_points() > other.score_to_points()

    def __lt__(self, other):
        return self.score_to_points() < other.score_to_points()

    def __ge__(self, other):
        return self.score_to_points() >= other.score_to_points()

    def __le__(self, other):
        return self.score_to_points() <= other.score_to_points()

    def __add__(self, other):
        return Score(self.goals + other.goals, self.points + other.points)

    def __sub__(self, other):
        return Score(self.goals - other.goals, self.points - other.points)

    def __iadd__(self, other):
        self = self + other
        return self

    def __isub__(self, other):
        self = self - other
        return self

    def __mul__(self, number):
        return Score(self.goals * number, self.points * number)

    def __rmul__(self, number):
        return Score(self.goals * number, self.points * number)

    def __imul__(self, num):
        self.goals = self.goals * num
        self.points = self.points * num
        return self

    def __str__(self):
        return '{} goal(s) and {} point(s)'.format(self.goals, self.points)
