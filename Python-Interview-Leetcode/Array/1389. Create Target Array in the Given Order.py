def createTargetArray(nums: list, index: list) -> list:
    length = len(nums)
    temp = [nums[0]]
    for i in range(1, length):
        temp.insert(index[i], nums[i])
    return temp