from typing import List


def findRepeatNumber(nums: List[int]) -> int:
    temp = [0] * len(nums)
    for i in nums:
        temp[i] += 1
    
    for i in range(len(nums)):
        if temp[i] > 1:
            print(i)
            return i


def findRepeatNumber1(nums: List[int]) -> int:
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                # 注意，不可用nums[i], nums[nums[i]] == nums[nums[i]], nums[i]来实现数据交换
                # 这和python底层实现有关，详见以下网页：
                # https://blog.csdn.net/qq_43029747/article/details/95992657
                
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]

#  解法3：直接进行排序，排序之后看相邻的两个元素是否相等，相等则表示是室友重复的元素的
        
if __name__ == '__main__':
    findRepeatNumber([2, 3, 1, 0, 2, 5, 3])