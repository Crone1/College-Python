
def matcher(s):
    d = {'(': ')',
         '{': '}',
         '[': ']'}

    l = []
    for c in s:
        if c in l:
            l.remove(c)

        else:
            if c in d:
                l.append(d[c])

            else:
                return False

    return not bool(l)
