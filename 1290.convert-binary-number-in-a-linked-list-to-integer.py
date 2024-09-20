#
# @lc app=leetcode.cn id=1290 lang=python3
# @lcpr version=30121
#
# [1290] 二进制链表转整数
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
    def getDecimalValue(self, head: ListNode) -> int:
        #先逆向链表
        list=[]
        while head:
          list.append(head.val)
          head=head.next
        #用list储存起来
        list.reverse()
        sum=0
        count=1
        #循环加到一起即可
        for i in list:
          sum+=i*count
          count*=2
        return sum
          
# @lc code=end



#
# @lcpr case=start
# [1,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0]\n
# @lcpr case=end

#

