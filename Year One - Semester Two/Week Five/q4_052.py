import sys

filename = sys.argv[1]
d = {}
keys = []
values = []

with open(filename, 'r') as f:
    for line in f.readlines():
        line = line.strip().split()
        d[' '.join(line[0:-1])] = int(line[-1])

final_d = {}

for line in sys.stdin:
    line = line.strip()
    i = 0
    while i < len(line) and line[i] != ',':
        i = i + 1

    if i < len(line):
        name = line[:i]
        final_d[name] = 0

    i = i + 1
    while i < len(line):
        j = i
        while i < len(line) and line[i] != ',':
            i = i + 1
        
        if line[j:i] in d:
            for key in d:
                if key == line[j:i]:
                    final_d[name] = final_d[name] + int(d[line[j:i]])

        else:
            final_d[name] = final_d[name] + 100

        i = i + 1

k_longest = 0
v_longest = 0
for k,v in final_d.items():
	if len(k) > k_longest:
	    k_longest = len(k)

	if len(str(v)) > v_longest:
		v_longest = len(str(v))

for k,v in final_d.items():
	keys.append(k)
	values.append(v)

vals = [val for val,_ in sorted(zip(values,keys))]
key = [k for _,k in sorted(zip(values,keys))]

l = 0
while l < len(vals):
	print('{:>{}} : {:>{}}'.format(key[l], k_longest, vals[l], v_longest))
	l = l + 1
