"""
Leetcode 35: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums contains distinct values sorted in ascending order.
-10^4 <= target <= 10^4

Français:
Étant donné un tableau trié d'entiers distincts et une valeur cible,
renvoie l'index de la valeur cible si celle-ci est présente.
Sinon, renvoie l'index à l'endroit où elle se trouverait si elle avait été insérée dans l'ordre.


中文：
给定一个已排序且不重复的整数数组和一个目标值，如果找到该目标值，则返回其索引。
如果未找到，则返回如果按顺序插入该目标值时，它应位于的索引位置。
"""