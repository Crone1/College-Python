import sys

dictionary = {'a': 0,
              'e': 0,
              'i': 0,
              'o': 0,
              'u': 0}

keys = []
values = []

sentence = sys.stdin.read().strip().lower()

for letter in sentence:
    try:
        dictionary[letter] += 1

    except KeyError:
        pass

for key in dictionary:
    values.append(dictionary[key])
    keys.append(key)

longest = 0
for value in values:
    if longest < len(str(value)):
        longest = len(str(value))

keys = [key for _,key in sorted(zip(values,keys))[::-1]]
values = [value for value,_ in sorted(zip(values,keys))[::-1]]

i = 0
while i < len(values):
    print('{} : {:>{}}'.format(keys[i], values[i], longest))
    i = i + 1
