#
#  Just a class to store the item and the next pointer
#


class Node:

    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a
# class attribute"


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None

    def count(self):
        ptr = self.head
        i = 0
        while ptr != None:
            i = i + 1
            ptr = ptr.next

        return i

    def __iter__(self):
        cursor = self.head
        while cursor is not None:
            yield cursor.item
            cursor = cursor.next

    def after(self, item):
        i = 0
        for k in self:
            i = i + 1
            if k == item:
                break

        j = 0
        for m in self:
            j = j + 1
            if j == i + 1:
                return m

    def before(self, item):
        '''i = 0
        for k in self:
            i = i + 1
            if k == item:
                break

        j = 0
        for m in self:
            if j == i - 1:
                return m.item
            j = j + 1'''

        ptr = self.head
        while ptr != None and ptr.next != None and ptr.next.item != item:
            ptr = ptr.next

        if ptr != None and ptr.next != None:
            return ptr.item

    def contains(self, value):
        for k in self:
            if k == value:
                return True

        return False

        '''ptr = self.head
        while ptr != None:
            
            if ptr == value:
                return True
                
            ptr = ptr.next
        return False'''

    def append(self, item):
        if self.is_empty():
            self.head = Node(item, None)
            
        else:
            ptr = self.head
            while ptr.next != None:
                ptr = ptr.next
                
            ptr.next = Node(item, None)

    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next
            
        return tmp_str

    def rotate(self):
        first = self.remove()
        self.append(first)