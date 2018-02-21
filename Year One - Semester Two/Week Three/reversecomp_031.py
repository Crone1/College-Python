
import sys

words = [line.strip() for line in sys.stdin if len(line.strip()) >= 5]
reverse_in_list = []


def bsearch(a, q):
    low = 0
    high = len(a)

    while low < high:
        mid = (high + low) // 2

        if a[mid].lower() < q:
            low = mid + 1

        else:
            high = mid

    return a[low].lower() == q

for word in words:
    if bsearch(words, word.lower()[::-1]):
        reverse_in_list.append(word)
    

print (reverse_in_list)
