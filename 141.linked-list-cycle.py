#
# @lc app=leetcode.cn id=141 lang=python3
# @lcpr version=30121
#
# [141] 环形链表
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      '''
      #单指针+Hash
      #因为如果是环就会一直在里面跑，所以不能直接遍历一遍
      #这里字典不方便直接使用，可以使用set()，这是一个不重复的元素集合，可以直接将我们所创建的类值作为元素储存
      dict1=set()
      cur=head
      while cur:#这里什么时候循环cur，什么时候循环cur.next要搞清楚
        if cur in dict1:
          return True
        dict1.add(cur)
        cur=cur.next
      return False
      '''
      #快慢指针
      fast=head
      slow=head
      while fast:
        if fast.next==None:
          return False
        fast=fast.next
        if fast==slow:
          return True
        slow=slow.next
        fast=fast.next
      return False
        
      
        
        
# @lc code=end



#
# @lcpr case=start
# [3,2,0,-4]\n1\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n0\n
# @lcpr case=end

# @lcpr case=start
# [1]\n-1\n
# @lcpr case=end

#

