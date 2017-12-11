
import sys


line = sys.stdin.read().split()

i = 0
while i < len(line):
   b = line[i].rstrip().split('/')
   sys.stdout.write(str(b[len(b)-1]) + '\n')
   i = i + 1
