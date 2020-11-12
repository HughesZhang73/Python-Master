# coding=utf-8
from typing import List


# 方法一：横向扫描
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        prefix, count = strs[0], len(strs)
        for i in range(1, count):
            prefix = self.lcp(prefix, strs[i])
            if not prefix:
                break
        return prefix
    
    def lcp(self, str1, str2):
        length, index = min(len(str1), len(str2)), 0
        while index < length and str1[index] == str2[index]:
            index += 1
        return str1[:index]

# 最快的方法
class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        str0 = min(strs)
        str1 = max(strs)
        
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0


# 方法二：纵向扫描
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]
            
        return strs[0]


# 方法三：分治
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        def lcp(start, end):
            if start == end:
                return strs[start]
            
            mid = (start + end) // 2
            lcpLeft, lcpRight = lcp(start, mid), lcp(mid + 1, end)
            minLength = min(len(lcpLeft), len(lcpRight))
            for i in range(minLength):
                if lcpLeft[i] != lcpRight[i]:
                    return lcpLeft[:i]
            return lcpLeft[:minLength]
        
        if not strs:
            return ""
        else:
            lcp(0, len(strs) - 1)
            
            
        
        


if __name__ == '__main__':
    solution = Solution1()
    a = solution.longestCommonPrefix(["dog","racecar","car"])
    print(a)
