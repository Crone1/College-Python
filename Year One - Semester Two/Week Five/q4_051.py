import sys

integers = []
nums = {}

total = 0

for line in sys.stdin:
    integers.append(line.strip())

    try:
        nums[line.strip()] += 1

    except KeyError:
        nums[line.strip()] = 1

for integer in integers:
    total = total + int(integer)

most_common = 0
biggest_key = ''

for k, v in nums.items():
    if v > most_common:
        most_common = v
        biggest_key = k


integers = sorted(integers)

if len(integers) % 2 == 1:
    median = int(integers[(len(integers)) // 2])

else:
    median = ((int(integers[(len(integers)) // 2]) +
               int(integers[((len(integers)) // 2) - 1])) / 2)


print('Mean: {:<.1f}'.format(total / len(integers)))
print('Mode: {:<.1f}'.format(float(biggest_key)))
print('Median: {:<.1f}'.format(median))
