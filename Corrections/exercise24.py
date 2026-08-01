"""
Leetcode 83: Remove Duplicates from Sorted List

Given the head of a sorted linked list, delete all duplicates such that each element appears only once.
Return the linked list sorted as well.

Example 1:

1 -> 1 -> 2
     ↓
   1 -> 2

Input: head = [1,1,2]
Output: [1,2]

Example 2:

1 -> 1 -> 2 -> 3 -> 3
          ↓
     1 -> 2 -> 3

Input: head = [1,1,2,3,3]
Output: [1,2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

Français:
À partir d'une liste chaînée triée, supprimez tous les doublons
de manière à ce que chaque élément n'apparaisse qu'une seule fois.
Renvoyez également la liste chaînée triée.

中文：
给定一个已排序的链表的表头，删除所有重复项，使得每个元素只出现一次。
同时返回该已排序的链表。
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def delete_duplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    """
    题目意思：
    给你一个已经按升序排列的链表，例如：1 → 1 → 2 → 3 → 3
    删除重复节点后变成：1 → 2 → 3
    注意：链表已经排好序，所以相同的数字一定挨在一起。

    核心思路：
    使用一个指针 current 从头开始遍历。
    每次比较：
    current.val
    current.next.val
    如果它们相等，说明下一个节点重复了，直接跳过：
    current.next = current.next.next
    如果不相等，才把指针向后移动：
    current = current.next
    """
    current = head

    while current is not None and current.next is not None:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next

    return head