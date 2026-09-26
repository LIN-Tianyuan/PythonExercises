"""
Leetcode 104: Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:
        3
       / \
      9  20
         / \
        15 7

Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-100 <= Node.val <= 100

Français:
Étant donné la racine d'un arbre binaire, renvoyer sa profondeur maximale.

La profondeur maximale d'un arbre binaire correspond au nombre de nœuds le long du chemin
le plus long allant du nœud racine jusqu'au nœud feuille le plus éloigné.

中文：
给定一棵二叉树的根节点，请返回该树的最大深度。

二叉树的最大深度是指从根节点到最远叶节点这条最长路径上的节点数量。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
