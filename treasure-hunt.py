
import sys
import os

file = 'start.txt'

while os.path.isfile(file):

      with open(file, 'r') as openfile:
         file = openfile.read().strip()

sys.stdout.write(file + '\n')