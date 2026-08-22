"""
Leetcode 94: Binary Tree Inorder Traversal

Given the root of a binary tree, return the inorder traversal of its nodes' values.


Example 1:

Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:

1
 \
 2
 /
3



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:

           1
          / \
          2  3
         / \  \
         4 5   8
           /\  /
           6 7 9


Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Français:
Étant donné la racine d'un arbre binaire, renvoyez la traversée en ordre intermédiaire des valeurs de ses nœuds.

中文：
给定一棵二叉树的根节点，返回其节点值的中序遍历结果。
"""


def inorder_traversal(root):
    # 把它理解成：每来到一个节点，都先去把左边处理完，再记录自己，最后处理右边。
    result = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)       # 左
        result.append(node.val)  # 根
        inorder(node.right)      # 右

    inorder(root)
    return result

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 构造二叉树
root = TreeNode(4)

root.left = TreeNode(2)
root.right = TreeNode(5)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(inorder_traversal(root))

