#
# @lc app=leetcode.cn id=21 lang=python3
# @lcpr version=30117
#
# [21] 合并两个有序链表
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      point=ListNode()
      answer=point
      while list1 and list2:
          if list1.val <list2.val:
            point.next=list1
            list1=list1.next
          else:
            point.next=list2
            list2=list2.next
          point=point.next
      point.next=list1 if list1 else list2
      return answer.next            
# @lc code=end



#
# @lcpr case=start
# [1,2,4]\n[1,3,4]\n
# @lcpr case=end

# @lcpr case=start
# []\n[]\n
# @lcpr case=end

# @lcpr case=start
# []\n[0]\n
# @lcpr case=end

#

