class Node:
    """ A node in a BST. It may have left and right subtrees """
    def __init__(self, item, left = None, right = None):
        self.item = item
        self.left = left
        self.right = right

class BST:
    """ An implementation of a Binary Search Tree """
    def __init__(self):
        self.root = None

    '''def add(self, item):
        """ Add this item to its correct position on the tree """
        # This is a non recursive add method. A recursive method would be cleaner.
        if self.root == None: # ... Empty tree ...
            self.root = Node(item, None, None) # ... so, make this the root
        else:
            # Find where to put the item
            child_tree = self.root
            while child_tree != None:
                parent = child_tree
                if item < child_tree.item: # If smaller ... 
                    child_tree = child_tree.left # ... move to the left
                else:
                    child_tree = child_tree.right

            # child_tree should be pointing to the new node, but we've gone too far
            # we need to modify the parent nodes
            if item < parent.item:
                parent.left = Node(item, None, None)
            elif item > parent.item:
                parent.right = Node(item, None, None)
            #else:
            #   equal ... don't add it to the set.'''

    def recurse_add(self, ptr, item):
        if ptr == None:
            return Node(item)
        elif item < ptr.item:
            ptr.left = self.recurse_add(ptr.left, item)
        elif item > ptr.item:
            ptr.right = self.recurse_add(ptr.right, item)
        return ptr
        
    def add(self, item):
        """ Add this item to its correct position on the tree """
        self.root = self.recurse_add(self.root, item)
                
    def is_present(self, item):
        lst = []
        l = self.recursive_is_present(self.root, item, lst)
        total = 0
        for i in l:
            if i == item:
                return True
                
        return False
            
        return total
        
    def recursive_is_present(self, ptr, item, lst):
        if ptr == None :  # Base Case
            return []

        else:
            if ptr.left == None and ptr.right == None:
                return [ptr.item]
                
            if ptr.right != None and ptr.left != None:
                return [ptr.item] + self.recursive_is_present(ptr.left, item, lst) + self.recursive_is_present(ptr.right, item, lst)
                
            elif ptr.right == None and ptr.left != None:
                return [ptr.item] + self.recursive_is_present(ptr.left, item, lst)
                
            elif ptr.right != None and ptr.left == None:
                return [ptr.item] + self.recursive_is_present(ptr.right, item, lst)

    def total(self):
        return self.recursive_total(self.root)
        
        
    def recursive_total(self, ptr):
        if ptr == None :  # Base Case
            return 0
        else:
            if ptr.left == None and ptr.right == None:
                return ptr.item
                
            if ptr.right != None and ptr.left != None:
                return ptr.item + self.recursive_total(ptr.left) + self.recursive_total(ptr.right)
                
            elif ptr.right == None and ptr.left != None:
                return ptr.item + self.recursive_total(ptr.left)
                
            elif ptr.right != None and ptr.left == None:
                return ptr.item + self.recursive_total(ptr.right)

    def height(self):
            return self.recursive_height(self.root)

    def recursive_height(self, ptr):
        if ptr == None:
            return 0
            
        elif ptr.left == None and ptr.right == None:
                return 1
                
        elif ptr.right != None and ptr.left != None:
            return 1 + max([self.recursive_height(ptr.left), self.recursive_height(ptr.right)])
            
        elif ptr.right == None and ptr.left != None:
            return 1 + self.recursive_height(ptr.left)
            
        elif ptr.right != None and ptr.left == None:
            return 1 + self.recursive_height(ptr.right)

    def count_Value_of_items(self, lo, hi):
        lst = []
        count = 0
        l = self.recursive_count_value_of_items(self.root, lst)
        for i in l:
            if int(i) >= lo and int(i) <= hi:
                count += 1
                
        return count
        
    def recursive_count_value_of_items(self, ptr, lst):

        if ptr != None:
            if ptr.left == None and ptr.right == None:
                return [ptr.item]
                
            if ptr.right != None and ptr.left != None:
                return [ptr.item] + self.recursive_count_value_of_items(ptr.left, lst) + self.recursive_count_value_of_items(ptr.right, lst)
                
            elif ptr.right == None and ptr.left != None:
                return [ptr.item] + self.recursive_count_value_of_items(ptr.left, lst)

                
            elif ptr.right != None and ptr.left == None:
                return [ptr.item] + self.recursive_count_value_of_items(ptr.right, lst)
        
        else:
            return lst

    def recursive_count_nodes(self, ptr):
        if ptr == None :  # Base Case
            return 0
        else:
            if ptr.left == None and ptr.right == None:
                return 1
                
            if ptr.right != None and ptr.left != None:
                return 1 + self.recursive_count_nodes(ptr.left) + self.recursive_count_nodes(ptr.right)
                
            elif ptr.right == None and ptr.left != None:
                return 1 + self.recursive_count_nodes(ptr.left)
                
            elif ptr.right != None and ptr.left == None:
                return 1 + self.recursive_count_nodes(ptr.right)

    def count_nodes(self):
        return self.recursive_count_nodes(self.root)

    def rec_is_max(bst, ptr):
        
        #print('r_h = {}'.format(bst.r_height(bst.root)))
        
        nodes = 0
        for i in range(bst.r_height(bst.root)):
            nodes += 2**i
            
        #print('c_n = {}'.format(count_nodes(bst)))
        #print('n = {}'.format(nodes))
            
        if nodes == count_nodes(bst):
            return True
            
        return False
            
    def is_maximal(bst):
        return rec_is_max(bst, bst.root)

    def count_leaves(self):
        return self.recursive_count_leaves(self.root)
        
    def recursive_count_leaves(self, ptr):
        if ptr == None:
            return 0
            
        elif ptr.right == None and ptr.left == None:
            return 1
            
        elif ptr.right == None and ptr.left != None:
            return self.recursive_count_leaves(ptr.left)
            
        elif ptr.left == None and ptr.right != None:
            return self.recursive_count_leaves(ptr.right)
            
        elif ptr.right != None and ptr.left != None:
            return self.recursive_count_leaves(ptr.right) + self.recursive_count_leaves(ptr.left)