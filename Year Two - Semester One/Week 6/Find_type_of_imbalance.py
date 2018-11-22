
def rotation_type(bst):
    lh = bst.r_height(bst.root.left)
    rh = bst.r_height(bst.root.right)
    
    if lh > rh:
        if bst.r_height(bst.root.left.left) > bst.r_height(bst.root.left.right):
            return 'll'
            
        else:
            return 'lr'
    
    elif rh > lh:
        if bst.r_height(bst.root.right.left) > bst.r_height(bst.root.right.right):
            return 'rl'
            
        else:
            return 'rr'
            