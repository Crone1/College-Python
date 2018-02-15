import sys

n = 20

a = sys.stdin.readlines()
x = []
y = []
#a = sorted(a)

#print a
#a = sorted(a)
#print 'a =', a

j = 0
while j < len(a):
   s = a[j].split()
 #  print s
   x.append(s[0])   #get all x co-ordinates into a list
   y.append(s[1])   #get all y co-ordinates into a list
   j = j + 1

#print 'X=', x
#print 'Y =', y

sys.stdout.write(' ' + '-' * 20 + '\n') #print first line

l = 0
while l < len(a): #start loop to look through points

   largest = 0
   m = 1
   while m < len(y):
      if int(y[m]) > int(y[largest]): #find position of largest y co-ordinate
         largest = m
      m = m + 1

   #print largest

   pos_of_all_that_num = []
   k = 0
   while k < len(y):
      if y[k] == y[largest]:            #make a list of all positions within list y of numbers that are the 
         pos_of_all_that_num.append(k)  #same as the previously found largest y co-ordinate
      k = k + 1

   #print pos_of_all_that_num

   smallest = pos_of_all_that_num[0]

   if len(pos_of_all_that_num) > 1:

      p = 1
      while p < len(pos_of_all_that_num):
         if int(x[pos_of_all_that_num[p]]) < int(x[smallest]):
            smallest = pos_of_all_that_num[p]
         p = p + 1                     #if 2 largest numbers find smallest x co-ordiate of them

   #print x[smallest],y[smallest]

      if smallest == pos_of_all_that_num[0]:
         second_smallest = pos_of_all_that_num[1]
                 #assign name 'second smallest' to the other x co-ordinate with largest y co-ordinate

      elif smallest == pos_of_all_that_num[1]:
   	     second_smallest = pos_of_all_that_num[0]

 #     print str(y[smallest]),str(x[smallest]) + '+' + str(y[second_smallest]),str(x[second_smallest])
 
#   else:
 #      print y[smallest],x[smallest]

   lines_till_next = n - int(y[largest]) - 1   #find no of lines between points

   i = 0
   while i < lines_till_next:
      sys.stdout.write('|' + (' ' * 20) + '|' + '\n') #print no of lines till next point
      i = i + 1

   n = int(y[largest])

   if len(pos_of_all_that_num) > 1:
      sys.stdout.write('|' + (' ' * int(x[smallest])) + '*' + (' ' * (int(x[second_smallest]) - int(x[smallest]) - 1)) + '*' + (' ' * (19 - int(x[second_smallest]))) + '|' + '\n')
                                                        #print points
      x.pop(smallest)
      x.pop(second_smallest)   #get rid of those x co-ordinates
      y.pop(largest)           #get rid of those y co-ordinates

   else:
      sys.stdout.write('|' + (' ' * int(x[smallest])) + '*' + (' ' * (19 - int(x[smallest]))) + '|' + '\n')
                                                             #print points

      x.pop(smallest)          #get rid of those x co-ordinates
      y.pop(largest)           #get rid of those y co-ordinates

   l = l + 1

sys.stdout.write(' ' + '-' * 20 + '\n')    #print last line
