import sys

for word in sys.stdin:
    i = 0
    while i < len(word) and word[i].lower() != 'e':
        i = i + 1

    if i < len(word) and 'e' not in word[i + 1:].lower():
        while i < len(word) and word[i].lower() != 'v':
            i = i + 1

        new = word[:i] + word[i + 1:]
        if i < len(word) and 'v' not in new.lower():
            while i < len(word) and word[i].lower() != 'i':
                i = i + 1

            new = word[:i] + word[i + 1:]
            if i < len(word) and 'i' not in new.lower():
                while i < len(word) and word[i].lower() != 'l':
                    i = i + 1

                new = word[:i] + word[i + 1:]
                if word[i].lower() == 'l' and 'l' not in new.lower():
                    print(word.strip())

