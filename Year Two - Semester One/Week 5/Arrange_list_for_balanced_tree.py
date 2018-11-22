
#   Arrange a list so that when added to a tree will cause the tree to be completely balanced


def rec_make_list(lst, new_lst=None):
    if new_lst == None:
        new_lst = []

    if len(lst) == 1:
        new_lst.append(lst[0])

    elif len(lst) == 2:
        new_lst.append(lst[0])
        new_lst.append(lst[1])

    else:
        middle = len(lst)//2
        new_lst.append(lst[middle])

        rec_make_list(lst[:middle], new_lst)
        rec_make_list(lst[middle + 1:], new_lst)

    return new_lst


def make_list(lst):
    return rec_make_list(sorted(lst))