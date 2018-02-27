import sys
import string

dictionary = {}
keys = []
values = []

words = sys.stdin.read().strip().lower().split()

for word in words:
    i = 0
    while i < len(word):
        if word[i] in string.punctuation and word[i] != "'":
            word = word[:i]
            break

        i = i + 1

    try:
        dictionary[word] += 1

    except KeyError:
        dictionary[word] = 1

for key in dictionary:
        keys.append(key)


i = 0
while i < len(keys):
    print('{} : {}'.format(sorted(keys)[i], dictionary[sorted(keys)[i]]))
    i = i + 1
