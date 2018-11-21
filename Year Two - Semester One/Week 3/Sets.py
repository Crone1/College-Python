def set_intersection(s1, s2):
    return s1.intersection(s2)

def set_stuff(a, b):
    union = a.union(b)
    return (union, a.issubset(b), b.issubset(a))

def unique_list(l):
    return list(set(l))