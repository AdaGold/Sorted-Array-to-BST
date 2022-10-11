class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

class Tree:
	def __init__(self):
		self.root = None

def arr_to_bst(arr):
    """ Given a sorted array, write a function to create a 
        Balanced Binary Search Tree using the elements in the array.
        Return the root of the Binary Search Tree.
    """
    new_tree = Tree()
    mid = len(arr)//2

    if arr:
        new_tree.root = arr[mid]
        return new_tree.root
    return None

    

# Please note one is not required to implement a self-balancing Binary Search Tree in order to solve this exercise.

# It is recommended to break the problem down recursively by first setting the root of the Binary Search Tree to the middle element of the array.

