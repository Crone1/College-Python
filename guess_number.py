#!usr/bin/env python

import secret_number

def play():
   low = 0
   high = 999
   mid = (high + 1)/2
   output = secret_number.guess(mid)  
   while output != 'correct':

      if output == 'too-low':
        low = mid

      else:
         high = mid

      mid = low + (high-low)/2

      output = secret_number.guess(mid)

def main():
   print play()

if __name__ == '__main__':
   main()