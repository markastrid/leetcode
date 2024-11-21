#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#
# https://leetcode.cn/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (51.14%)
# Likes:    1171
# Dislikes: 0
# Total Accepted:    299.5K
# Total Submissions: 573.2K
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回
# 需要移除区间的最小数量，使剩余区间互不重叠 。
#
# 注意 只在一点上接触的区间是 不重叠的。例如 [1, 2] 和 [2, 3] 是不重叠的。
#
#
#
# 示例 1:
#
#
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#
#
# 示例 2:
#
#
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#
#
# 示例 3:
#
#
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#
#
#
#
# 提示:
#
#
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
#
#
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        # 使用 sorted 函数和 lambda 表达式按子列表的最后一个元素排序
        sorted_intervals = sorted(intervals, key=lambda x: x[-1])
        # 在这个例子中，lambda x: x[-1]是一个匿名函数，它接受一个参数x（在这里x代表intervals中的每个子列表），并返回x的最后一个元素（x[-1]）。sorted()函数使用这个返回值来决定排序的顺序。
        removed = 0
        ans = [sorted_intervals[0]]
        for i in range(1, len(sorted_intervals)):
            if ans[-1][-1] <= sorted_intervals[i][0]:
                ans.append(sorted_intervals[i])
                continue
            removed += 1
        return removed


# @lc code=end
