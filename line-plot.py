
import sys

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

slope = (y1 - y2)/(x1 - x2)

c = y1 - (slope * x1)

sys.stdout.write(' ' + '-' * 20 + '\n')

i = 0
while i < 20:
   y = 19 - i
   sys.stdout.write('|')

   x = 0
   while x < 20:

      if ((y > y1 and y > y2) or (y < y1 and y < y2)) or ((x < x1 and x < x2) or (x > x1 and x > x2)) or (x != int(((y - c)/slope) + 0.5) and y != int(slope * x + c + 0.5)):
         sys.stdout.write(' ')

      elif x == int(((y - c)/slope) + 0.5) or y == int(slope * x + c + 0.5):
         sys.stdout.write('*')

      x = x + 1

   if x == 20:
      sys.stdout.write('|' + '\n')

   i = i + 1

sys.stdout.write(' ' + '-' * 20 + '\n')