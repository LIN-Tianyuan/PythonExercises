"""
Leetcode 100: Same Tree

Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
    1                    1
    /\                   /\
   2 3                   2 3

Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
    1                     1
    /                     \
    2                     2

Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
    1                      1
    /\                     /\
    2 1                    1 2

Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104

Français:
Écrivez une fonction qui, à partir des racines de deux arbres binaires p et q, vérifie s'ils sont identiques ou non.
Deux arbres binaires sont considérés comme identiques s'ils sont structurellement identiques
et si leurs nœuds ont la même valeur.

中文：
给定两个二叉树 p 和 q 的根节点，编写一个函数来判断它们是否相同。
如果两个二叉树在结构上完全相同，且节点的值也相同，则认为它们是相同的。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
