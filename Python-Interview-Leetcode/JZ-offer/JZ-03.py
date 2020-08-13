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
                # ע�⣬������nums[i], nums[nums[i]] == nums[nums[i]], nums[i]��ʵ�����ݽ���
                # ���python�ײ�ʵ���йأ����������ҳ��
                # https://blog.csdn.net/qq_43029747/article/details/95992657
                
                temp = nums[i]
                nums[i], nums[temp] = nums[temp], nums[i]

#  �ⷨ3��ֱ�ӽ�����������֮�����ڵ�����Ԫ���Ƿ���ȣ�������ʾ�������ظ���Ԫ�ص�
        
if __name__ == '__main__':
    findRepeatNumber([2, 3, 1, 0, 2, 5, 3])