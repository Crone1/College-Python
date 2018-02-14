import sys

print 'What is Your Variable Name?'
x = sys.stdin.read(1)

print 'What is Your Equation?'
print '(Use Two Asctriscs To Indicate To The Power Of)'

s = sys.stdin.read().strip()

i = 0
while i < len(s) and s[i] != x:
   i = i + 1

print 'a'

if i < len(s):
   a = s[:i]
   
   j = i + 1
   while j < len(s) and s[j] != x:
      j = j + 1

   print 'b'

   if j < len(s):
      b = s[i + 5:j]

      l = j + 1
      while l < len(s):
         l = l + 1
         
      print 'c'

      if l == len(s):
         c = s[j + 2:l]
         
   else:
      print '!!!!   Error, This is not a Quadratic   !!!!'
      
else:
   print '!!!!   Error, Wrong Variable Name Given   !!!!'

print 'r'


a = float(int(a))
b = float(int(b))
c = float(int(c))

in_sqr_root = (b**2) - (4 * a * c)

sqr_root = (int(in_sqr_root))**(0.5)

bottom = 2 * a

minus_b = -b

equation_plus = (minus_b + sqr_root) / bottom

equation_minus = (minus_b - sqr_root) / bottom

print 'x = ' + str(equation_plus), 'AND', 'x = ' + str(equation_minus)