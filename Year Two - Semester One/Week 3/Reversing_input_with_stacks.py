from Stack import Stack
import sys

def reverse_input(stack):
    # Your code here
    lines = sys.stdin.readlines()
    for line in lines:
        stack.push(line.strip())
    while stack.top > 0:
        print(stack.pop())