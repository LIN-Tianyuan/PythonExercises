
def two_sum(nums, target):
    for index_a in range(len(nums)):
        for index_b in range(index_a + 1, len(nums)):
            if nums[index_a] + nums[index_b] == target:
                return [index_a, index_b]

print(two_sum([2, 3, 4], 6))
