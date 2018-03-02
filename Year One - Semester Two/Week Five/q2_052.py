import sys


def contains(word):
    i = 0
    while i < len(word) and word[i].lower() != 'a':
        i = i + 1

    if i < len(word) and 'a' not in word[i + 1:].lower():
        j = i
        while j < len(word) and word[j] != 'e':
            j = j + 1

        if j < len(word) and 'e' not in word[j + 1:].lower():
            j = i
            while j < len(word) and word[j] != 'i':
                j = j + 1

            if j < len(word) and 'i' not in word[j + 1:].lower():
                j = i
                while j < len(word) and word[j] != 'o':
                    j = j + 1

                if j < len(word) and 'o' not in word[j + 1:].lower():
                    j = i
                    while j < len(word) and word[j] != 'u':
                        j = j + 1

                    return j < len(word) and 'u' not in word[j + 1:].lower()

    return False

def main():
    for word in sys.stdin:
        if contains(word.strip()):
            print(word.strip())


if __name__ == '__main__':
    main()
