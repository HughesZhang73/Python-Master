# conding = utf-8

# 暴力相加，直接累加超时，优化判断条件后————狗过！！！
# class Solution:
#     def pivotIndex(self, nums: List[int]) -> int:
#         length = len(nums)
#         pivot = 0
#         if length == 1 or length == 2 or length == 0:
#             pivot = -1
#             return pivot
#         elif length == 3:
#             if nums[0] == nums[2]:
#                 pivot = -1
#                 return pivot
#             else:
#                 pivot = -1
#                 return pivot
#         else:
#             while pivot != length:
#                 left_sum = sum(nums[pivot])
#                 if nums[pivot] == sum(nums) - 2 * left_sum:
#                     return pivot
#                 else:
#                     pivot += 1
#                     continue
#             return -1


# 前缀和解决

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        left_sum = 0
        for i, x in enumerate(nums, 0):
            if left_sum == S - left_sum - nums[x]:
                return i
            left_sum += x
        return -1
    
# 内存占用最少
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1
    
# 执行速度最快

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        res = sum(nums)
        sum_l = 0
        for i in range(len(nums)):
            sum_l += nums[i]
            if sum_l - nums[i] == res - sum_l:
                return i
        return -1