# @lcpr-before-debug-begin
from python3problem2 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=2 lang=python3
# @lcpr version=30117
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      if not l1:
        return l2
      if not l2:
        return l1
      l1.val=l1.val+l2.val
      if l1.val>=10:
        l1.next=self.addTwoNumbers(ListNode(1),l1.next)#注意这个之前直接写成1了，符号不对,应该是自己设置的类类型
        l1.val=l1.val-10
      l1.next=self.addTwoNumbers(l1.next,l2.next)
      return l1
# @lc code=end



#
# @lcpr case=start
# [2,4,3]\n[5,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n[0]\n
# @lcpr case=end

# @lcpr case=start
# [9,9,9,9,9,9,9]\n[9,9,9,9]\n
# @lcpr case=end

#

