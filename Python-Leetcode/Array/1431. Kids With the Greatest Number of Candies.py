def kidsWithCandies(candies: list, extraCandies: int) -> list:
    ans = []
    candies = tuple(candies)
    for i in range(len(candies)):
        temp = candies[i] + extraCandies
        if candies[i] >= max(candies):
            ans.append(bool(1))
        else:
            ans.append(bool(0))
    return ans


print(kidsWithCandies([2, 3, 5, 1, 3], 3))