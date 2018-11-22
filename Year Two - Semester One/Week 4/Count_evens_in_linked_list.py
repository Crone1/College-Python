def even_count(lst):
    '''def __iter__(lst):
        cursor = list.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    a = []
    for number in lst:
        a.append(number)

    i = 0
    for number in a:
        if number % 2 == 0:
            i = i + 1

    return i'''

    ptr = lst.head
    i = 0
    while ptr != None:
        if not ptr.item % 2:
            i = i + 1
        ptr = ptr.next

    return i
