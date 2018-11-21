def get_sliced_lists(l):
    except_last = l[:-1]
    except_first_nd_last = l[1:-1]
    reverse = l[len(l)::-1]
    
    return [except_last, except_first_nd_last, reverse]