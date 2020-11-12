class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda x: x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # print(s[left: right])
                return isPalindrome(s[left + 1: right + 1]) or isPalindrome(s[left: right])
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.validPalindrome('axsa'))

