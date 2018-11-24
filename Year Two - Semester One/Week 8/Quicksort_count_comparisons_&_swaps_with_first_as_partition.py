#
#   qsort code and a partition function.
#
#   Modify the code so that it returns the number of compares and the number of moves.
#
def partition(lst, lo, hi):
    global comps, moves
    part = lo

    while lo < hi:
        while lst[lo] <= lst[part] and lo < hi:
            lo += 1
            comps += 1

        comps += 1

        while lst[hi] > lst[part]: # Don't have to check for hi >= 0 cos part is there as a sentinel.
            hi -= 1
            comps += 1
        comps += 1

        if lo < hi:
            # Swap the two entries
            lst[hi], lst[lo] = lst[lo], lst[hi]
            moves += 3

    # Swap part into position
    if lst[part] > lst[hi]: # (this may happen of the array is small (size 2))
        moves += 3
        lst[part], lst[hi] = lst[hi], lst[part]

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