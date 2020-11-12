# def shuffle(nums: list, n: int) -> list:
#     temp1 = nums[0:n]
#     temp2 = nums[n:n << 1]
#     temp3 = []
#     a = 0
#     b = 0
#     for i in range(n << 1):
#         if i % 2 == 0:
#             temp3.append(temp1[a])
#             a = a + 1
#         else:
#             temp3.append(temp2[b])
#             b = b + 1
#     return temp3


# def shuffle(nums: list, n: int) -> list:
#     episode = 1
#     while (episode << 1) - 1 < n:
#         print((episode << 1) - 1)
#         temp = (episode << 1) - 1
#
#         head_num = nums[n]
#         tail_num = nums[n - 1]
#         nums.remove(head_num)
#         nums.remove(tail_num)
#
#         nums.insert(temp, head_num)
#         nums.insert((n << 1) - temp - 1, tail_num)
#
#         episode += 1
#     return nums


def shuffle(nums, n):
    nums[::2], nums[1::2] = nums[:n], nums[n:]
    return nums


# print(shuffle([2, 5, 1, 3, 4, 7], 3))
# print(shuffle([1, 1, 2, 2], 2))
# print(shuffle([1, 2, 3, 4, 4, 3, 2, 1], 4))
print(shuffle([7, 5, 9, 7, 5, 8, 10, 4, 3, 3, 2, 5, 9, 10], 7))
