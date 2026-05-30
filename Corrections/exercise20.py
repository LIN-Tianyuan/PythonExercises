"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

Français:
On vous donne un grand nombre entier représenté par un tableau d'entiers `digits`,
où chaque élément `digits[i]` correspond au ième chiffre de ce nombre entier.
Les chiffres sont classés du plus significatif au moins significatif, de gauche à droite.
Ce grand nombre entier ne comporte aucun 0 en tête.

中文：
给定一个大整数，该整数由整数数组 digits 表示，其中每个 digits[i] 代表该整数的第 i 位。
这些数字按从最高位到最低位的顺序从左到右排列。
该大整数不包含任何前导 0。
"""

from typing import List

def plus_one(digits: List[int]) -> List[int]:
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0

    return [1] + digits