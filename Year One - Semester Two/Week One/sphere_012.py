import sys
import math

def main():
	start_radius = sys.argv[1]
	radius_increment = sys.argv[2]
	ending_radius = sys.argv[3]

	h1 = 'Radius (m)'
	h4 = '-' * len(h1)
	h2 = 'Area (m^2)'
	h5 = '-' * len(h2)
	h3 = 'Volume (m^3)'
	h6 = '-' * len(h3)

	print ('{:>s} {:>15s} {:>15s}'.format(h1, h2, h3))
	print ('{:>s} {:>15s} {:>15s}'.format(h4, h5, h6))

	range_between = float(ending_radius) - float(start_radius)
	number_per_num = 1 / float(radius_increment)

	i = 0
	while i < int(range_between * number_per_num) + 1:
		first = float(start_radius) + (float(radius_increment) * i)
		area = 4 * math.pi * (first ** 2)
		volume = 4/3 * math.pi * (first ** 3)
		print ('{:>10.1f} {:>15.2f} {:>15.2f}'.format(first, area, volume))
		i = i + 1

if __name__ == '__main__':
	main()