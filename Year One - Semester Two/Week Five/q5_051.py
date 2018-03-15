import sys
name_and_best_time = {}
time_seconds = []


def sorter(t):
    return seconds(t[-1])


def seconds(time):
    [mins, secs] = time.split(':')
    time_seconds = (int(mins) * 60) + int(secs)
    return time_seconds

for line in sys.stdin:
    tokens = line.strip().split()
    name = tokens[0]
    times = tokens[1:]

    try:
        name_and_best_time[name] = min(times, key=seconds)

    except ValueError:
        continue

[k, v] = min(name_and_best_time.items(), key=sorter)

print('{} : {}'.format(k, v))
