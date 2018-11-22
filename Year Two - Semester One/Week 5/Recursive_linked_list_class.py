#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
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



    def recursive_count(self, ptr):

        if ptr == None:
            return 0
        else:
            
            return  1 + self.recursive_count(ptr.next)

    def count(self):
        return self.recursive_count(self.head)



    def recursive_count_even(self, ptr):
        if ptr == None:
            return 0
            
        elif ptr.item % 2 == 0:
            return 1 + self.recursive_count_even(ptr.next)
            
        else:
            return self.recursive_count_even(ptr.next)

    def count_even(self):
        return self.recursive_count_even(self.head)



    def r_present(ptr, item):
        if ptr == None:
            return False
        elif ptr.item == item:
            return True

        else:
            return r_present(ptr.next, item)

    def is_present(self, item):
        return r_present(self.head, item)



    def recursive_max(self, ptr):
        if ptr == None:
            return -1000000000000000000000000
            
        return max([ptr.item, self.recursive_max(ptr.next)])
        
    def largest(self):
        return self.recursive_max(self.head)



    def recursive_duplicates(self, ptr):
        if self.is_empty() or ptr.next == None:
            return False
            
        return (not (ptr.item == ptr.next.item)) == self.recursive_diplicates(ptr.next)


    def Consecative_duplicates(self):
        return self.recursive_diplicates(self.head)
