def swap_keys_values(d):
    keys = []
    values = []
    dic = {}

    for k, v in d.items():
        keys.append(k)
        values.append(v)

    i = 0
    while i < len(values):
        dic[values[i]] = keys[i]
        i = i + 1

    return dic