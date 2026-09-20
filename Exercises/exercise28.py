"""
Leetcode 101: Symmetric Tree

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


Example 1:
        1
       / \
       2  2
      / \ / \
      3 4 4 3

Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:
        1
       / \
      2  2
      \  \
      3  3

Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?

Français:
Étant donné la racine d'un arbre binaire, vérifiez s'il s'agit d'une image miroir de lui-même
(c'est-à-dire s'il est symétrique par rapport à son centre).

中文：
给定一棵二叉树的根节点，判断该树是否是其自身的镜像（即以中心为轴对称）。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
