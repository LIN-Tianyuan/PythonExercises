"""
Leetcode 108: Convert Sorted Array to Binary Search Tree

Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.


Example 1:
             0
           /  \
          -3  9
          /   /
        -10  5

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

        0
       / \
     -10  5
       \   \
       -3   9

Example 2:
        3    1
       /     \
      1      3

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.


Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in a strictly increasing order.

Français:
Étant donné un tableau d'entiers `nums` dont les éléments sont triés par ordre croissant,
convertissez-le en un arbre de recherche binaire équilibré en hauteur.

中文：
给定一个整数数组 nums，其中元素按升序排列，
将其转换为高度平衡的二叉搜索树。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""

"""
Leetcode Solution

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])

    root.left = sorted_array_to_bst(nums[:mid])
    root.right = sorted_array_to_bst(nums[mid + 1:])

    return root

def print_tree(root, level=0, prefix="Root: "):
    if root is not None:
        print("    " * level + prefix + str(root.val))

        print_tree(root.left, level + 1, "L--- ")
        print_tree(root.right, level + 1, "R--- ")

if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]

    root = sorted_array_to_bst(nums)

    print_tree(root)
