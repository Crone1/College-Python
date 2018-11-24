""" Selection sort algorithm """
def selection_sort(lst):
    comps = 0
    moves = 0
    
    for i in range(len(lst) - 1):
        # Find the smallest item in the lst starting at i
        min_index = i
        
        for j in range(min_index + 1, len(lst)):
            comps += 1
            if lst[j] < lst[min_index]:
                
                min_index = j
        # place smallest at the beginning (swap min index with i)
        if i != min_index:
            lst[i], lst[min_index] = lst[min_index], lst[i] # Don't swap if already in position
            moves += 3
            
    return (comps, moves)