#
#   qsort code and a partition function.
#
#   Modify the partition function so that it uses the middle element.
#
def partition(lst, lo, hi):
    global comps, moves
    mid = ((lo + hi )// 2)
    lst[lo], lst[mid] = lst[mid], lst[lo]
    moves += 3
    part = lo
    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            comps += 1
            lo += 1
        comps += 1
        
        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            comps += 1
            hi -= 1
        comps += 1
        
        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            moves += 3

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        lst[part], lst[hi] = lst[hi], lst[part]
        moves += 3
        
    comps += 1
    return hi, comps, moves

def rec_qsort(lst, lo, hi):
    global comps, moves
    if lo < hi:
        pivot, comps, moves = partition(lst, lo, hi)
        rec_qsort(lst, lo, pivot - 1)
        rec_qsort(lst, pivot + 1, hi)
    return (comps, moves)
    
def qsort(lst):
    global comps, moves
    comps = 0
    moves = 0
    rec_qsort(lst, 0, len(lst) - 1)
    return (comps, moves)