class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

def arr_to_bst_helper(arr, start, end):
    if not arr:
        return None

    if start == end:
        return TreeNode(arr[start])

    mid = start + (end - start) // 2
    node = TreeNode(arr[mid])

    if start <= mid - 1:
        node.left = arr_to_bst_helper(arr, start, mid - 1)
    if mid + 1 <= end:
        node.right = arr_to_bst_helper(arr, mid + 1, end)

    return node

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """

    return arr_to_bst_helper(arr, 0, len(arr) - 1)