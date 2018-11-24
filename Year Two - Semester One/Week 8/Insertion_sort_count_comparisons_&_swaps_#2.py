def insertion_sort(lst):
    times_moved = 0
    compares = 0

    for todo in range(1, len(lst)):
        tobeinserted = lst[todo]
        i = todo
        while i > 0 and tobeinserted < lst[i-1]:
            compares += 1
            times_moved += 1

            lst[i] = lst[i-1] # Make space for the item
            i -= 1

        if i > 0:
            compares += 1

        lst[i] = tobeinserted  # Found the place for this item, plonk it in
        times_moved += 2

    return (compares, times_moved)