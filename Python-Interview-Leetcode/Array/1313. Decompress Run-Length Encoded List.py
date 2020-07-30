def decompressRLElist(nums: list) -> list:
    length = len(nums)
    temp = []
    for i in range(0, length, 2):
        temp += [nums[i + 1]] * nums[i]
    return temp


print(decompressRLElist([1,2,3,4]))