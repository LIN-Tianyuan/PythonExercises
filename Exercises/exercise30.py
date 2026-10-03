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