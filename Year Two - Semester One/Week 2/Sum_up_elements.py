
def sum_to_k(lst, k):
    i = 0
    while i < len(lst):
        j = 0
        while j < len(lst) and i != j:
            if lst[i] + lst[j] == k:
                return True
            j = j + 1
        i = i + 1

    return False
