# coding=gbk
# def processQueries(queries: list, m: int) -> list:
#     temp = []
#     ans = []
#     length = len(queries)
#     for i in range(1, m + 1):
#         temp.append(i)
#     for i in range(length):
#         # print('查询列表遍历元素: {qur}'.format(qur=queries[i]))
#         # print("temp position:")
#         print(temp.index(queries[i]))
#         ans.append(temp.index(queries[i]))
#         temp.remove(queries[i])
#         temp.insert(0, queries[i])
#     return ans


print(processQueries([7,5,5,8,3], 8))
