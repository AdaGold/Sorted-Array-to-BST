class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right


def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    while arr: 
        medi = (len(arr)) // 2
        root = TreeNode(arr[medi])
        root.left = arr_to_bst(arr[:medi])
        root.right = arr_to_bst(arr[medi+1:])   
        return root
    else: 
        return None