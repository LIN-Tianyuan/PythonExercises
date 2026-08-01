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