def make_edge_list(adjacency):
    """ this function create an edge list representation of a graph using the supplied adjacency matrix
    """
    edge_list = []
    import string
    d = dict(enumerate(string.ascii_uppercase, 0))
    
    for lst in adjacency:
        i = 0
        new = []
        while i < len(lst):
            if lst[i] != 0:
                new.append(d[i])
            i = i + 1
            
        edge_list.append(new)

    return edge_list
