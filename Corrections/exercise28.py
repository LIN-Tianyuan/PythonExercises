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

"""
Leetcode Solution

class Solution:
    def isSymmetric(self, root):
        def check(left, right):
            # 两边都是 None
            if left is None and right is None:
                return True

            # 只有一边是 None
            if left is None or right is None:
                return False

            # 当前两个节点值必须相同
            if left.val != right.val:
                return False

            # 镜像比较
            return (
                    check(left.left, right.right)
                    and
                    check(left.right, right.left)
            )
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root):
    # 可以理解成：我给你两个节点，你帮我判断它们是不是互为镜像。
    def check(left, right):
        # 两边都是 None
        if left is None and right is None:
            return True

        # 只有一边是 None
        if left is None or right is None:
            return False

        # 当前两个节点值必须相同
        if left.val != right.val:
            return False

        # 镜像比较
        return (
                check(left.left, right.right)
                and
                check(left.right, right.left)
        )

    return check(root.left, root.right)

if __name__ == "__main__":
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    print(is_symmetric(root))