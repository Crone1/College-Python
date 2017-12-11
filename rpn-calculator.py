import sys
import math
 
stack = []
user_input = sys.stdin.read()
tokens = user_input.split()

def add(a,b):
  return a + b

def subtract(a,b):
   return a - b

def multiply(a,b):
   return a * b

def divide(a,b):
   return a / b

def remainder(a,b):
   return a % b

def power(a,b):
   return a ** b

def negative(a):
   return -a

def square(a):
   return a * a

def square_root(a):
   return math.sqrt(a)

def log(a):
   return math.log(a)

def integer(a):
   return (a.isdigit()) or (2 <= len(a) and a[1:].isdigit() and a[0] == '-')

def floating_point(a):
   return len(a.split('.')) == 2 and integer(a.split('.')[0]) and a.split('.')[1].isdigit()

binary_operations = {'+': add,
                     '-': subtract,
                     '*': multiply,
                     '/': divide,
                     '%': remainder,
                     '**': power}

unary_operations = {'n': negative,
										's': square,
										'r': square_root,
										'l': log}

i = 0
while i < len(tokens):

   if integer(tokens[i]):
      stack.append(int(tokens[i]))

   elif floating_point(tokens[i]):
      stack.append(float(tokens[i]))

   elif tokens[i] in binary_operations:
      b = stack.pop()
      a = stack.pop()
      c = binary_operations[tokens[i]](a,b)
      stack.append(c)

   elif tokens[i] in unary_operations:
      b = stack.pop()
      a = unary_operations[tokens[i]](b)
      stack.append(a)

   elif tokens[i] == 'p':
      print stack[len(stack) - 1]
   i = i + 1