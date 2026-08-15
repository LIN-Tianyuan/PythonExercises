"""
Leetcode 88: Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.



Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[j] <= 109


Follow up: Can you come up with an algorithm that runs in O(m + n) time?

Français:
On vous donne deux tableaux d'entiers, nums1 et nums2, triés par ordre non décroissant,
ainsi que deux entiers m et n, représentant respectivement le nombre d'éléments de nums1 et de nums2.

Fusionnez nums1 et nums2 en un seul tableau trié par ordre non décroissant.

中文：
给定两个整数数组 nums1 和 nums2，它们按非递减顺序排序，
以及两个整数 m 和 n，分别表示 nums1 和 nums2 中的元素个数。

将 nums1 和 nums2 合并为一个按非递减顺序排序的数组。
"""

def merge(nums1, m, nums2, n):
    """
    三个指针，从后往前
    为什么从后面开始？

    因为 nums1 后面本来就是空位：

    nums1
    [1, 2, 3, 0, 0, 0]
     ↑        ↑
     i        k

    nums2
    [2, 5, 6]
     ↑
     j

    设置：

    i = m - 1      # nums1有效部分最后一个
    j = n - 1      # nums2最后一个
    k = m + n - 1  # nums1最终数组最后一个

    然后比较 nums1[i] 和 nums2[j]。

    谁大，就把谁放到 nums1[k]。

    比如：

    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]

    比较 3 和 6
    6 大

    nums1 = [1,2,3,0,0,6]

    然后：

    比较 3 和 5
    5 大

    nums1 = [1,2,3,0,5,6]

    然后：

    比较 3 和 2
    3 大

    nums1 = [1,2,3,3,5,6]

    继续比较即可。
    """
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1

        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)

