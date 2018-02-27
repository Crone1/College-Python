import sys
import string

dictionary = {'a': 0,
              'e': 0,
              'i': 0,
              'o': 0,
              'u': 0}

keys = []
values = []

words = sys.stdin.read().strip().lower()

for letter in sentence:
    try:
        dictionary[letter] += 1

    except KeyError:
        pass

for key in dictionary:
    keys.append(key)

i = 0
while i < len(keys):
    print('{} : {:>3}'.format(sorted(keys)[i], dictionary[sorted(keys)[i]]))
    i = i + 1
