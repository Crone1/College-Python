
class Stack(object):

    def __init__(self):
        self.l = []

    def push(self, other):
        self.l.append(other)

    def pop(self):
        return self.l.pop()

    def top(self):
        return self.l[-1]

    def is_empty(self):
        return not bool(self.l)

    def __len__(self):
        return len(self.l)
