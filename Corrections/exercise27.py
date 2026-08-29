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

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p, q):
    # Both nodes are empty
    # If, at the current position, neither tree has any nodes
    if p is None and q is None:
        return True

    # One is empty, and the other is not empty
    if p is None or q is None:
        return False

    # The current node values are different
    if p.val != q.val:
        return False

    # As before, compare the left and right subtrees.
    return (
        is_same_tree(p.left, q.left)
            and
        is_same_tree(p.right, q.right)
    )

# Create the First Tree [1, 2, 3]
p = TreeNode(1)
p.left = TreeNode(2)
p.right = TreeNode(3)

# Create the Second Tree [1, 2, 3]
q = TreeNode(1)
q.left = TreeNode(2)
q.right = TreeNode(3)


print(is_same_tree(p, q))