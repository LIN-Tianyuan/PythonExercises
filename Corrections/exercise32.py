"""
Leetcode 111: Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
        3
       / \
      9  20
         /\
        15 7

Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 10^5].
-1000 <= Node.val <= 1000
"""

"""
Leetcode Solution

class Solution:
    def minDepth(self, root):
        if root is None:
            return 0

        # 左子树为空，只能走右边
        if root.left is None:
            return 1 + self.minDepth(root.right)

        # 右子树为空，只能走左边
        if root.right is None:
            return 1 + self.minDepth(root.left)

        # 左右都存在，才可以取最小值
        return 1 + min(
            self.minDepth(root.left),
            self.minDepth(root.right)
        )
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def min_depth(root):
    """
    La profondeur minimale correspond au nombre de nœuds entre la racine et la feuille la plus proche.
    Attention : si un nœud n'a qu'un seul enfant, on ne peut pas choisir le côté vide. On doit continuer
    dans le sous-arbre qui existe.
    :param root:
    :return:
    """
    if root is None:
        return 0

    if root.left is None:
        return 1 + min_depth(root.right)

    if root.right is None:
        return 1 + min_depth(root.left)

    return 1 + min(
        min_depth(root.left),
        min_depth(root.right)
    )


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


print(min_depth(root))