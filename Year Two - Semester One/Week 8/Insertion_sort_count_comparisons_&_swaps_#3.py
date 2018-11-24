#
#   Insertion Sort
#
#   First place the smallest element at the front of the list to act as a sentinel
#
def insertion_sort(lst):
    moves = 0
    comps = 0
    if len(lst) == 0:
        return

    # Find the smallest element
    min_index = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_index]:
            min_index = i;

    # Move smallest to the front (swap elements min_index and 0)
    lst[0], lst[min_index] = lst[min_index], lst[0]
    moves += 1

    # Now, with the smallest in the front, we don't need to check i in the inner loop
    
    # At each pass ensure that that section is sorted (start at 2, cos smallest already in position).
    for todo in range(2, len(lst)):
        # Find correct position for lst[todo]
        store = lst[todo]
        i = todo
        while store < lst[i-1]: # Don't need to check i > 0
            moves += 1
            comps += 1
            lst[i] = lst[i-1] # Make space for the item
            i -= 1
        comps += 1
        moves += 2
        lst[i] = store  # Found the place for this item, plonk it in
    comps = comps + (len(lst) + 1)
    return (moves, comps)