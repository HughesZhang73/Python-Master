class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [start]
        for i in range(1, n):
            nums[0] ^= start + (i << 1)
        return nums[0]