

def swap_unique_keys_values(d):
    kv = []
    dic = {}
    seen = {}

    for k, v in d.items():
        kv.append((v, k))

    seen[kv[0][0]] = False

    for t in kv:
        if t[0] not in seen:
            seen[t[0]] = False
        else:
            seen[t[0]] = True

    for t in kv:
        if not seen[t[0]]:
            dic[t[0]] = t[1]

    return dic