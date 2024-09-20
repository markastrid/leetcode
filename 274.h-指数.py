#
# @lc app=leetcode.cn id=274 lang=python3
#
# [274] H 指数
#
# https://leetcode.cn/problems/h-index/description/
#
# algorithms
# Medium (44.52%)
# Likes:    528
# Dislikes: 0
# Total Accepted:    224.6K
# Total Submissions: 485.9K
# Testcase Example:  '[3,0,6,1,5]'
#
# 给你一个整数数组 citations ，其中 citations[i] 表示研究者的第 i 篇论文被引用的次数。计算并返回该研究者的 h 指数。
#
# 根据维基百科上 h 指数的定义：h 代表“高引用次数” ，一名科研人员的 h 指数 是指他（她）至少发表了 h 篇论文，并且 至少 有 h
# 篇论文被引用次数大于等于 h 。如果 h 有多种可能的值，h 指数 是其中最大的那个。
#
#
#
# 示例 1：
#
#
# 输入：citations = [3,0,6,1,5]
# 输出：3
# 解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
# 由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
#
# 示例 2：
#
#
# 输入：citations = [1,3,1]
# 输出：1
#
#
#
#
# 提示：
#
#
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
#
#
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        '''
        # 下面是我用的最朴素的方法进行计算
        # 首先，h肯定要从最大开始，也就是长度
        H = len(citations)
        # 以下是H种可能，从大到小
        for i in range(H, 0, -1):
            # print(i)
            # 这个是用作计数有多少篇超过H次
            count = 0
            for j in range(H):
                # print(citations[j])
                if citations[j] >= i:
                    count += 1
                if count == i:
                    return i
        return 0
        '''
        # 下面是优化的:我们发现只需要对数组进行排序之后，从最小的开始进行寻找，这时候h=0
        Sorted_Cite = sorted(citations, reverse=True)
        h = 0
        # 在循环中，我们如果发现某某个Sorted_Cite大于h，那么就至少找到了一个新的h=h+1，以此类推到h无法增大
        for i in range(len(Sorted_Cite)):
          if Sorted_Cite[i] > h:
            h += 1
        return h
        # @lc code=end
