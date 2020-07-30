def numIdenticalPairs(nums: list):
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count


# def numIdenticalPairs(nums: list):
#     i, ans, num = 0, 0, sorted(nums)
#     for j in range(1, len(nums)):
#         if nums[i] == nums[j]:
#             ans += (j - i)
#         else:
#             i = j


# def numIdenticalPairs(nums: list):
#     nums = tuple(nums)
#     ans = 0
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 ans += 1
#     return ans

print(numIdenticalPairs([4, 4, 2, 2]))
