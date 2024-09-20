# @lcpr-before-debug-begin
from python3problem83 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=83 lang=python3
# @lcpr version=30121
#
# [83] 删除排序链表中的重复元素
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
      if not head:
        return head
      temp=head
      while head.next:
        if head.val==head.next.val:
          head.next=head.next.next
        else:#注意这里需要if+else，因为if的条件出现后，head还需要和下一个比较，要是直接移走到下一个链表元素就少了一次比较
          head=head.next
      return temp
# @lc code=end



#
# @lcpr case=start
# [1,1,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,1,2,3,3]\n
# @lcpr case=end

#

