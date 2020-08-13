#coding=utf-8


class Solution:
    def MinCost(self, board_length):
        ans = 0
        n = len(board_length)
        while n > 1:
            min1 = 0
            min2 = 1
            if board_length[min1] > board_length[min2]:
                temp = board_length[min1]
                board_length[min1] = board_length[min2]
                board_length[min2] = temp
            
            for i in range(2, n):
                if board_length[i] < board_length[min1]:
                    min2 = min1
                    min1 = i
                elif board_length[i] < board_length[min2]:
                    min2 = i
            
            # 结合木板
            
            t = board_length[min1] + board_length[min2]
            ans += t
            
            if min1 == n - 1:
                temp1 = min1
                min1 = min2
                min2 = temp1
            
            board_length[min1] = t
            board_length[min2] = board_length[n - 1]
            n -= 1
        return ans
    

if __name__ == '__main__':
    b = [8, 5, 8]
    s = Solution()
    print(s.MinCost(b))

    

