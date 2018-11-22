from LinkedList import LinkedList

class LinkedStack:
    def __init__(self):
        self.ll = LinkedList()

    def push(self, item):
        class Node:
            def __init__(self, item, next):
                self.item = item
                self.next = next

        self.ll.head = Node(item, self.ll.head)

    def pop(self):
        if not self.ll.is_empty():
            item = self.ll.head.item
            self.ll.head = self.ll.head.next
            try:
                return int(item)
                
                
            except ValueError:
                return str(item)

    def is_empty(self):
        ptr = self.ll.head
        while ptr != None:
            ptr = ptr.next

        return ptr == self.ll.head

        '''return self.ll.head == None'''