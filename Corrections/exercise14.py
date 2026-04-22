"""
Leetcode 21: Merge Two Sorted Lists
English:
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]

Example 2:

Input: list1 = [], list2 = []
Output: []

Example 3:

Input: list1 = [], list2 = [0]
Output: [0]


Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.

Français:
On vous donne les têtes de deux listes chaînées triées, list1 et list2.
Fusionnez les deux listes en une seule liste triée. Cette liste doit être constituée en concaténant les nœuds des deux premières listes.
Renvoyez la tête de la liste chaînée fusionnée.

中文：
已给定两个已排序链表 list1 和 list2 的头节点。
将这两个链表合并为一个已排序的链表。该链表应通过将前两个链表的节点拼接在一起生成。
返回合并后链表的头节点。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    dummy = ListNode()   # 虚拟头节点
    cur = dummy

    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next

    # 把没走完的那部分直接接上
    cur.next = list1 if list1 else list2

    return dummy.next

if __name__ == '__main__':
    def build_linked_list(arr):
        dummy = ListNode()
        cur = dummy
        for num in arr:
            cur.next = ListNode(num)
            cur = cur.next
        return dummy.next

    def print_linked_list(head):
        while head:
            print(head.val, end=" -> ")
            head = head.next
        print("None")


    list1 = build_linked_list([1,2,4])
    list2 = build_linked_list([1,3,4])

    result = merge_two_lists(list1, list2)

    print_linked_list(result)
