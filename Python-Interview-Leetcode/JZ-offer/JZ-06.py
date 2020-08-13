# coding=utf-8

from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# # 方法一：直接进行链表的额反转操作，将链表的数据存入到列表钟
# class Solution:
#     def reversePrint(self, head: ListNode) -> List[int]:
#         current = head
#         pre_node = None
#
#         while current:
#
#             temp = current.next
#             current.next = pre_node
#
#             pre_node = current
#             current = temp
#
#         head = pre_node
#
#         ans = []
#
#         while head is not None:
#             ans.append(head.val)
#             head = head.next
#         return ans


# #  方法二：利用递归的特性求解
# class Solution:
#     def reversePrint(self, head: ListNode) -> List[int]:
#         return self.reversePrint(head.next) + [head.val] if head else []
#

# python目前时间最快方法
class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res[::-1]
