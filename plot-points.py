
import sys

n = 20

a = sys.stdin.readlines()
x = []
y = []

j = 0
while j < len(a):
   s = a[j].split()
   x.append(s[0])   #get all x co-ordinates into a list
   y.append(s[1])   #get all y co-ordinates into a list
   j = j + 1

sys.stdout.write(' ' + '-' * 20 + ' ' + '\n') #print first line

l = 0
while l < len(a): #start loop to look through points

   largest = 0
   m = 1
   while m < len(y):
      if y[m] > y[largest]: #find position of largest y co-ordinate
         largest = m
      m = m + 1

   pos_of_all_that_num = []

   k = 0
   while k < len(y):
      if y[k] == y[largest]:   #note position of all of the largest numbers
         pos_of_all_that_num.append(k)
      k = k + 1

   smallest = pos_of_all_that_num[0]
   p = 1
   while p < len(pos_of_all_that_num) and len(pos_of_all_that_num) > 1:
      if x[pos_of_all_that_num[p]] < x[smallest]:
         smallest = pos_of_all_that_num[p]      #if 2 largest numbers find smallest x co-ordiate of the lot
      p = p + 1

   if len(pos_of_all_that_num) > 1 and smallest == pos_of_all_that_num[0]:
   	second_smallest = pos_of_all_that_num[1]
                                           #there are only max 2 numbers with same y co-ordinate
   elif len(pos_of_all_that_num) > 1 and smallest == pos_of_all_that_num[1]:
   	second_smallest = pos_of_all_that_num[0]

   lines_till_next = n - int(y[largest]) - 1   #find no of y co-ordinates between points

   i = 0
   while i < lines_till_next:
      sys.stdout.write('|' + (' ' * 20) + '|' + '\n') #print no of lines till next y co-ordiante
      i = i + 1

   n = int(y[largest])

   if len(pos_of_all_that_num) > 1:
      sys.stdout.write('|' + (' ' * int(x[smallest])) + '*' + (' ' * (int(x[second_smallest]) - int(x[smallest]))) + (' ' * (19 - int(x[second_smallest]))) + '|' + '\n')
      
      x.pop(smallest)
      x.pop(second_smallest)   #get rid of largest numbers
      y.pop(largest)

   else:
      sys.stdout.write('|' + (' ' * int(x[largest]) + '*' + (' ' * (19 - int(x[smallest]))) + '|' + '\n'))

      x.pop(smallest)             #get rid of largest number
      y.pop(largest)

   l = l + 1

sys.stdout.write(' ' + '-' * 20 + ' ')    #print last line