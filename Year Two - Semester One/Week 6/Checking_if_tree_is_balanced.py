def recur_avl_tree(BST, ptr):
    if ptr == None:
        return True
        
    lh = BST.r_height(ptr.left)
    rh = BST.r_height(ptr.right)
    
    if (abs(lh - rh) <= 1) and recur_avl_tree(BST, ptr.left) and recur_avl_tree(BST, ptr.right):
        return True
        
    return False
    
def is_avl(bst):
    return recur_avl_tree(bst, bst.root)