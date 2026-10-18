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
"""

def merge_two_lists(list1, list2):

    if len(list1)>50 and len(list2)>50:
        return False
    for i in list1:
        if i>100 or i<-100:
            return False
    for i in list2:
        if i>100 or i<-100:
            return False

    res=[]
    i=0
    j=0
    while i < len(list1) and j < len(list2):
        # manipuler avc les pointeurs
        if list1[i] <= list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    # ajouter ce qui reste a la fin de la liste si la longeur des deux listes sont differentes
    res.extend(list1[i:]) # si i == len(list1), alors list1[i:] est une liste vide on ajoute rien
    res.extend(list2[j:])
    return res

print(merge_two_lists([1, 2, 4], [1, 3, 4]))
print(merge_two_lists([], []))
print(merge_two_lists([], [0]))
print(merge_two_lists([1,4,5,6], [1,1,5]))