from Node import Node

#
#   Function to add an item to a tree.
#
#   This is not good object oriented coding. It's not even very polite. It directly interferes with the tree's innards.
#
def add(tree, item):
    
    """ Add this item to its correct position on the tree """
    
    # This is a non recursive add method. A recursive method would be cleaner.
    if tree.root == None: # ... Empty tree ...
        tree.root = Node(item, None, None) # ... so, make this the root
    else:
        # Find where to put the item
        child_tree = tree.root
        parents_list = []
        
        while child_tree != None:
            
            parent = child_tree
            parents_list.append(parent)
            if item < child_tree.item: # If smaller ... 
                child_tree = child_tree.left # ... move to the left
            elif item > child_tree.item:
                child_tree = child_tree.right

        # child_tree should be pointing to the new node, but we've gone too far
        # we need to modify the parent nodes
        if item < parent.item:
            parent.left = Node(item, None, None)
        elif item > parent.item:
            parent.right = Node(item, None, None)
        # Ignore the case where the item is equal.
        

    def recur_avl_tree(BST, ptr):
        if ptr == None:
            return True

        lh = BST.recurse_height(ptr.left)
        rh = BST.recurse_height(ptr.right)

        if (abs(lh - rh) <= 1) and recur_avl_tree(BST, ptr.left) and recur_avl_tree(BST, ptr.right):
            return True

        return False
        
    
    if not recur_avl_tree(tree, tree.root):
        for parent in parents_list[::-1]:
            if not recur_avl_tree(tree, parent):
                return parent.item

    #   Note that you can get the height of a node by calling tree.recurse_height().
    #       For example, the height of the root is tree.recurse_height(tree.root)