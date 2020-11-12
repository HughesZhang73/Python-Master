def findNumbers(nums: list) -> int:
    ans = 0
    for i in nums:
        count = 1
        while i >= 10:
            i = i / 10
            count += 1
        if count % 2 == 0:
            ans += 1
    return ans


print(findNumbers([100000]))