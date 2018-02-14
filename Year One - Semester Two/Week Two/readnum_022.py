import sys

for n in sys.stdin:
	n = n.strip()
	try:
		n = int(n)
		print ('Thank you for {}'.format(n))
		break
	except:
		print ('{} is not a number'.format(n))