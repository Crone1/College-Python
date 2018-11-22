from LinkedList import LinkedList

class HashSet:
    def __init__(self, capacity=10):
        # Create a list to use as the hash table
        self.table = [None] * capacity

    def add(self, item):
        # Find the hash code
        h = hash(item)
        index = h % len(self.table)

        # Check is it empty
        if self.table[index] == None:
            self.table[index] = LinkedList() # Need a new linked list for this entry

        if item not in self.table[index]:
            # Only add it if not already there (this is a set)
            self.table[index].add(item)
            
    def average_bucket_length(self):
        total = 0
        i = 0
        for item in self.table:
            if item:
                i += 1
                total = total + len(item)
        return (total / i)

    def min_max_bucket_length(self):
        lists = {}
        for linked_list in self.table:
            if linked_list:
                lists[len(linked_list)] = linked_list
                
        #for k,v in lists.items():
        #   print('k = {}'.format(k))
        #   print (v)
        
        #for k in lists.keys():
        maximum = max(lists.keys())
        minimum = min(lists.keys())
        
        #print ( 'max = {}'.format(maximum))
        
        return (minimum, maximum)

    def __iter__(self):
        r_list = []
        for i in self.table:
            if i and len(i) > 1:
                pointer = i.head
                while pointer != None:
                    yield (pointer.item)
                    pointer = pointer.next
            elif i:
                yield (i.head.item)

