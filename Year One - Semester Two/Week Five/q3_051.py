import sys

for word in sys.stdin:
    most_upper = ''
    word = word.strip()

    i = j = 0
    while i < len(word) and j < len(word):

        while i < len(word) and word[i].islower():
            i = i + 1

        j = i + 1
        while j < len(word) and word[j].isupper():
            j = j + 1

        if len(word[i:j]) > len(most_upper):
            most_upper = word[i:j]
        i = j

    print(most_upper)
