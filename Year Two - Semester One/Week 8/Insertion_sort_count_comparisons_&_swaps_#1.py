def insertion_sort(lst):
    comp_count = 0
    swap_count = 0
    
    # At each pass ensure that that section is sorted.
    for todo in range(1, len(lst)):
        # Find correct position for lst[todo].
        i = todo
        while i > 0 and lst[i] < lst[i-1]:
            
            comp_count += 1
            swap_count += 1

            lst[i], lst[i-1] = lst[i-1], lst[i] # Swap it down towards the correct position
            i -= 1
        if i > 0:
            comp_count += 1
    return comp_count, swap_count