
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

sys.stdout.write(' ' + '-' * 20 + '\n') #print first line

while y: #start loop to look through points

   largest = 0
   m = 1
   while m < len(y):
      if int(y[m]) > int(y[largest]): #find position of largest y co-ordinate
         largest = m
      m = m + 1

   pos_of_all_that_num = []
   k = 0
   while k < len(y):
      if y[k] == y[largest]:            #make a list of all positions within list y of numbers that are the 
         pos_of_all_that_num.append(k)  #same as the previously found largest y co-ordinate
      k = k + 1

#   z = 0
#   while z < len(pos_of_all_that_num):
#      print y[largest], x[pos_of_all_that_num[z]]
#      z = z + 1

   numb_same_y_value = len(pos_of_all_that_num)

   smallest = pos_of_all_that_num[0]
   second_smallest = ''
   third_smallest = ''

   if len(pos_of_all_that_num) > 1:

      small = 0
      p = 1
      while p < len(pos_of_all_that_num):
         if int(x[pos_of_all_that_num[p]]) < int(x[pos_of_all_that_num[small]]):
            small = p
         p = p + 1                     #if 2 largest numbers find smallest x co-ordiate of them

      smallest = pos_of_all_that_num[small]
      pos_of_all_that_num.pop(small)

      if len(pos_of_all_that_num) > 1:
         sec_small = 0
         p = 1
         while p < len(pos_of_all_that_num):
            if int(x[pos_of_all_that_num[p]]) < int(x[pos_of_all_that_num[sec_small]]):
               sec_small = p
            p = p + 1                     #if 2 largest numbers find smallest x co-ordiate of them

         second_smallest = pos_of_all_that_num[sec_small]
         pos_of_all_that_num.pop(sec_small)

         third_smallest = pos_of_all_that_num[0]

      else:
         second_smallest = pos_of_all_that_num[0]

#   if smallest and second_smallest and third_smallest:
#      print 'third=', str(y[smallest]),str(x[smallest]) + '+' + str(y[second_smallest]),str(x[second_smallest]) + '+' + str(y[third_smallest]), str(x[third_smallest])
      
#   elif smallest and second_smallest:
#   	print 'second=', str(y[smallest]),str(x[smallest]) + '+' + str(y[second_smallest]),str(x[second_smallest])

#   else:
#      print 'one=', y[smallest],x[smallest]

   lines_till_next = n - int(y[largest]) - 1   #find no of lines between points

   i = 0
   while i < lines_till_next:
      sys.stdout.write('|' + (' ' * 20) + '|' + '\n') #print no of lines till next point
      i = i + 1

   n = int(y[largest])

   if numb_same_y_value == 3:
      if int(x[second_smallest]) - int(x[smallest]) != 0:
         sys.stdout.write('|' + (' ' * int(x[smallest])) + '*' + (' ' * (int(x[second_smallest]) - int(x[smallest]) - 1)) + '*' + (' ' * (int(x[third_smallest]) - int(x[second_smallest]) - 1)) + '*' + (' ' * (19 - int(x[third_smallest]))) + '|' + '\n')

      else:
         sys.stdout.write('|' + (' ' * int(x[smallest])) + '*' + (' ' * (int(x[third_smallest]) - int(x[smallest]) - 1)) + '*' + (' ' * (19 - int(x[third_smallest]))) + '|' + '\n')

      number = y[largest]

      y.pop(largest)
      x.pop(largest)

      w = 0
      while w < len(y) and y[w] != number:
         w = w + 1

      if w < len(y):
         y.pop(w)
         x.pop(w)

      w = 0
      while w < len(y) and y[w] != number:
         w = w + 1

      if w < len(y):
         y.pop(w)
         x.pop(w)

   elif numb_same_y_value == 2:
      sys.stdout.write('|' + (' ' * int(x[smallest])) + '*' + (' ' * (int(x[second_smallest]) - int(x[smallest]) - 1)) + '*' + (' ' * (19 - int(x[second_smallest]))) + '|' + '\n')
                                                        #print points
      number = y[largest]

      y.pop(largest)
      x.pop(largest)

      w = 0
      while w < len(y) and y[w] != number:
         w = w + 1

      if w < len(y):
         y.pop(w)
         x.pop(w)
      
   elif numb_same_y_value == 1:
      sys.stdout.write('|' + (' ' * int(x[smallest])) + '*' + (' ' * (19 - int(x[smallest]))) + '|' + '\n')
                                                             #print points
      x.pop(largest)          #get rid of those x co-ordinates
      y.pop(largest)           #get rid of those y co-ordinates

sys.stdout.write(' ' + '-' * 20 + '\n')    #print last line