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
    if arr == []:
        return None
    
    left = 0
    right = len(arr) -1
    return binary_search_in_arr(arr, left, right)
    

def binary_search_in_arr(arr, left, right):
    if arr == []:
        return None
    if right >= left:
        mid = left + (right - left) // 2
        node = TreeNode(arr[mid])
        node.right = binary_search_in_arr(arr, mid+1, right)
        node.left = binary_search_in_arr(arr, left , mid - 1)
        return node
    return None