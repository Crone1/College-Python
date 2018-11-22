def detect_loop(lst):
    ptr = lst.head
    
    while ptr != None and ptr.next != None and ptr.next != lst.head:
        ptr = ptr.next
        
    if ptr == None or ptr.next == None:
        return False
    
    if ptr.next == lst.head:
        return True