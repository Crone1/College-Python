
import sys
pattern = sys.argv[1]
replacement = sys.argv[2]

line = raw_input()
while line != 'END':
    new = ''

    i = 0
    while i < len(line):
        j = i
        while j < len(line) and line[j:j + len(pattern)] != pattern:
            j = j + 1

        new = new + line[i:j]

        if j < len(line):
            new = new + replacement
            
        i = j + len(pattern)

    print new
    line = raw_input()
