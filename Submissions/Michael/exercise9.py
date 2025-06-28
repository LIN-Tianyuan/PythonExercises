"""Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]


Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists."""

lista = []
def two_sum(nums, target):
    found = False
    a = 0
    b = 0
    for element in lista:
        for  element2 in lista:
            if element + element2 == target:
                a = nums.index(element)
                b = nums.index(element2)
                print(f"[{a}, {b}]")
                found = True
                break
        if found:
            break


# while True:
#     num = input("num = ")
#     if num == "stop":
#         break
#     lista.append(int(num))
#
# target = int(input("target = "))
# print(lista)
# two_sum(lista, target)

lista = [3, 4, 2]
print(two_sum(lista, 7))