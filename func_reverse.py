#!usr/bin/env python

def swap(a,i,j):
   temp = a[i]
   a[i] = a[j]
   a[j] = temp

def reverse(a):
   i = 0
   j = len(a) -1
   while i < j:
      swap(a,i,j)
      i = i + 1
      j = j - 1

def main():
   a = [4, 3, 2, 1]
   print swap(a,2,3)
   print reverse(a)

if __name__ == '__main__':
   main()