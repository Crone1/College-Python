import sys
from stack_092 import Stack
import math


def calculator(line):

    changers_b = {'+': lambda a, b: a + b,
                  '-': lambda a, b: a - b,
                  '*': lambda a, b: a * b,
                  '/': lambda a, b: a / b,
                  '%': lambda a, b: a % b,
                  '**': lambda a, b: a ** b}

    changers_u = {'n': lambda a: -a,
                  's': lambda a: a * a,
                  'r': lambda a: math.sqrt(a),
                  'l': lambda a: math.log(a)}

    stack = Stack()
    line = line.strip().split()

    for i in range(0, len(line)):

        if line[i] in changers_b:
            try:
                one = float(stack.pop())
                two = float(stack.pop())
                stack.push(changers_b[line[i]](two, one))

            except (ValueError, IndexError):
                break
                

        elif line[i] in changers_u:

            try:
                one = float(stack.pop())
                stack.push(changers_u[line[i]](one))

            except ValueError:
                break

        elif line[i].split('.')[0].isdigit():
            stack.push(line[i])

    if len(stack) == 1:
        return float(stack.l[0])

    else:
        raise IndexError("What's up bro?")
