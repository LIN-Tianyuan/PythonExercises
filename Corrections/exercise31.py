"""
Leetcode 110: Balanced Binary Tree

Given a binary tree, determine if it is height-balanced.

Example 1:
        3
       / \
      9  20
         /\
        15 7

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:
                1
               / \
              2  2
             /\
            3 3
           /\
          4 4
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-10^4 <= Node.val <= 10^4
"""

"""
Leetcode Solution

class Solution:
    def isBalanced(self, root):
        if root is None:
            return True

        left_height = self.height(root.left)
        right_height = self.height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        if root is None:
            return 0

        return 1 + max(
            self.height(root.left),
            self.height(root.right)
        )
"""

# class TreeNode:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def is_balanced(root):
    return height(root) != -1

def height(root):
    if root is None:
        return 0

    left_height = height(root.left)
    if left_height == -1:
        return -1

    right_height = height(root.right)
    if right_height == -1:
        return -1

    if abs(left_height - right_height) > 1:
        return -1

    return 1 + max(left_height, right_height)


# 测试 1：平衡二叉树
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

print(is_balanced(root1))
# True


# 测试 2：不平衡二叉树
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.left.left = TreeNode(3)

print(is_balanced(root2))
# False