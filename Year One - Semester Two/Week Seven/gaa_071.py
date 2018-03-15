
class Score(object):

    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def greater_than(self, s2):
        return ((self.goals * 3) + self.points) > ((s2.goals * 3) + s2.points)

    def less_than(self, s2):
        return ((self.goals * 3) + self.points) < ((s2.goals * 3) + s2.points)

    def equal_to(self, s2):
        return ((self.goals * 3) + self.points) == ((s2.goals * 3) + s2.points)
