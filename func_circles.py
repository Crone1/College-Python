#!usr/bin/env python

def circumference(r):
   return 6.282 * r

def area(r):
   return 3.141 * (r ** 2)

def main():
   print circumference(2)
   print area(3)

if __name__ == '__main__':
   main()