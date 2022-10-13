import pytest
from binary_search_trees.array_to_bst import *


def test_will_return_balanced_bst_for_odd_lengthed_list():
    # Arrange
    arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]

    # Act
    answer = arr_to_bst(arr)

    # Assert
    assert answer.val is 25 and is_bst(answer) and is_balanced_tree(answer)

def test_will_return_balanced_bst_for_even_lengthed_list():
    # Arrange
    arr = [1, 3, 9, 27, 81, 243]

    # Act
    answer = arr_to_bst(arr)

    # Assert
    assert is_bst(answer) and is_balanced_tree(answer) 

def test_will_return_balanced_bst_for_long_list():
    # Arrange
    arr = []
    num = 0
    while num < 100:
        arr.append(num)
        num += 1

    # Act
    answer = arr_to_bst(arr)

    # Assert
    assert is_bst(answer) and is_balanced_tree(answer)

def test_will_return_none_for_empty_list():
    # Arrange
    arr = []

    # Act
    answer = arr_to_bst(arr)

    # Assert
    assert answer is None
    

# Below are functions used to test if the given tree is a balanced Binary Search Tree.

# Returns True if the BST provided is a valid BST.
def is_bst(root):
    if root is None:
        return True

    left = root.left
    if left is not None and root.val <= left.val:
        return False

    right = root.right
    if right is not None and root.val >= right.val:
        return False

    return is_bst(left) and is_bst(right)

# Returns the height of a tree
def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


# Returns True if a tree is balanced
def is_balanced_tree(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    left_check = is_balanced_tree(root.left)
    right_check = is_balanced_tree(root.right)

    return left_check and right_check
