#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
# https://leetcode.cn/problems/linked-list-cycle/description/
#
# algorithms
# Easy (51.55%)
# Likes:    2224
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.6M
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给你一个链表的头节点 head ，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos
# 来表示链表尾连接到链表中的位置（索引从 0 开始）。注意：pos 不作为参数进行传递 。仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环 ，则返回 true 。 否则，返回 false 。
#
#
#
# 示例 1：
#
#
#
#
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
#
#
# 示例 2：
#
#
#
#
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
#
#
# 示例 3：
#
#
#
#
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
#
#
#
#
# 提示：
#
#
# 链表中节点的数目范围是 [0, 10^4]
# -10^5 <= Node.val <= 10^5
# pos 为 -1 或者链表中的一个 有效索引 。
#
#
#
#
# 进阶：你能用 O(1)（即，常量）内存解决此问题吗？
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        '''
        # 哈希表：需要额外空间
        ans = set()
        while head:
            # 直接存head这个链表结构就是为了防止val一样的情况，所以不能存head.val
            if head in ans:
                return True
            ans.add(head)
            head = head.next
        return False
        '''
        # 快慢指针：不需要额外空间
        if head == None or head.next == None:
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if fast==None or fast.next==None:
                return False
            slow=slow.next
            fast=fast.next.next
        return True
            # @lc code=end
