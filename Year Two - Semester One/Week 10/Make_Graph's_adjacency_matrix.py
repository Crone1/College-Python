def make_adjacency_matrix(edge_list):
    """ this function create an adjacency matrix representation of a graph using the supplied edge list
    """
    # Maybe start with an empty adjacency matrix
    adjacency_matrix = []
    letters = []
    letter_d = {}
    import string
    for char in string.ascii_uppercase:
        letters.append(char)
    i = 0

    while i < len(letters):
        letter_d[letters[i]] = i
        i = i + 1

    maxitem = 0
    for lst in edge_list:
        for item in lst:

            if letter_d[item] > maxitem:
                maxitem = letter_d[item]
                
    for lst in edge_list:
        base_list = [0] * (maxitem + 1)

        for item in lst:
            i = 0
            while i < len(letters):
                if item == letters[i]:
                    base_list[i] = 1
                i = i + 1
        
        adjacency_matrix.append(base_list)
    return adjacency_matrix
