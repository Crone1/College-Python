def build_dictionary(filename):
    d = {}

    with open(filename, 'r') as f:
        for line in f.readlines():
            [string, integer] = line.strip().split()
            d[string] = int(integer)

    return d


def extract_range(d, low, high):
    new_d = {}
    for k, v in d.items():
        if low <= v <= high:
            new_d[k] = v

    return new_d