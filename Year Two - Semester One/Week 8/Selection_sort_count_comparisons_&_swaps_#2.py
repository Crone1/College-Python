"""
    Selection sort algorithm

    This version of selection sort simultaneously gets the smallest and the largest
    and swaps them with the first and last element respectively.
    
    Timing tests show that it is about 7% faster on random input of size 10000
    
    Is it worth the extra effort?
    No. Use an NlogN algorithm instead for 1000* improvement.

"""
def selection_sort(lst):
    comps = 0
    moves = 0
    lo = 0
    hi = len(lst) - 1
    while lo < hi:
        
        min_index = lo
        max_index = lo
        for j in range(lo + 1, hi + 1):
            comps += 2
            if lst[j] < lst[min_index]:
                comps -= 1
                min_index = j
            elif lst[j] >= lst[max_index]: # maybe >= to get stable sort

                max_index = j
            
        if max_index == lo:

            max_index = min_index   # We will be moving lst[lo] to min_index, so update max_index first

        # swap min index with lo ... place smallest at the first
        lst[lo], lst[min_index] = lst[min_index], lst[lo]
        moves += 3
        # swap max index with hi ... place largest at the end
        lst[hi], lst[max_index] = lst[max_index], lst[hi]
        moves += 3
        lo += 1
        hi -= 1
    
    return (comps, moves)