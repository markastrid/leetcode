#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode.cn/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (66.54%)
# Likes:    3678
# Dislikes: 0
# Total Accepted:    1.9M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
#
#
#
# 示例 1：
#
#
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
#
#
# 示例 2：
#
#
# 输入：l1 = [], l2 = []
# 输出：[]
#
#
# 示例 3：
#
#
# 输入：l1 = [], l2 = [0]
# 输出：[0]
#
#
#
#
# 提示：
#
#
# 两个链表的节点数目范围是 [0, 50]
# -100
# l1 和 l2 均按 非递减顺序 排列
#
#
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list3 = ListNode()
        head = list3
        print(head)
        while list1 and list2:
            if list1.val < list2.val:
                list3.next = list1
                list3 = list3.next
                list1 = list1.next
            else:
                list3.next = list2
                list3 = list3.next
                list2 = list2.next
        if not list1:
            list3.next = list2
        if not list2:
            list3.next = list1
        # 之所以用head.next是因为默认建立链表的时候有一个空的链表头
        
        return head.next

# @lc code=end
