# coding=utf-8

from typing import List


# # 做法1：列表复制
#
# class Solution:
#
#     def replaceSpace(self, s: str) -> str:
#         for i in s:
#             temp.append(i)
#         for i in temp:
#             if i == ' ':
#                 temp_index = temp.index(' ')
#                 temp.remove(i)
#                 temp.insert(temp_index, '%20')
#         for i in temp:
#             ans += i
#         return ans


# 做法二：使用双指针进行列表的复制
class Solution:
    
    def replaceSpace(self, s: str) -> str:
        temp = ''
        for i in range(len(s)):
            if s[i] == ' ':
                temp += '%20'
            else:
                temp += s[i]
        return temp

#
# # 解法三：线性自己遍历赋值
# class Solution:
#     def replaceSpace(self, s: str) -> str:
#         return '%20'.join(s.split(' '))


if __name__ == '__main__':
    ss = Solution()
    print(ss.replaceSpace("hello world"))
