#
# @lc app=leetcode.cn id=234 lang=python3
# @lcpr version=30121
#
# [234] 回文链表
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
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #先逆向链表
        list1=[]
        while head:
          list1.append(head.val)
          head=head.next
        #用list储存起来
        #reversed(list)是迭代器对象，必须把它重新变为列表
        list2=list(reversed(list1))
        if list1==list2:
          return True
        return False
# @lc code=end



#
# @lcpr case=start
# [1,2,2,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

