#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#
# https://leetcode.cn/problems/minimum-number-of-arrows-to-burst-balloons/description/
#
# algorithms
# Medium (50.79%)
# Likes:    1025
# Dislikes: 0
# Total Accepted:    318.4K
# Total Submissions: 609.6K
# Testcase Example:  '[[10,16],[2,8],[1,6],[7,12]]'
#
# 有一些球形气球贴在一堵用 XY 平面表示的墙面上。墙面上的气球记录在整数数组 points ，其中points[i] = [xstart, xend]
# 表示水平直径在 xstart 和 xend之间的气球。你不知道气球的确切 y 坐标。
#
# 一支弓箭可以沿着 x 轴从不同点 完全垂直 地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足
# xstart ≤ x ≤ xend，则该气球会被 引爆 。可以射出的弓箭的数量 没有限制 。 弓箭一旦被射出之后，可以无限地前进。
#
# 给你一个数组 points ，返回引爆所有气球所必须射出的 最小 弓箭数 。
#
#
# 示例 1：
#
#
# 输入：points = [[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# -在x = 6处射出箭，击破气球[2,8]和[1,6]。
# -在x = 11处发射箭，击破气球[10,16]和[7,12]。
#
# 示例 2：
#
#
# 输入：points = [[1,2],[3,4],[5,6],[7,8]]
# 输出：4
# 解释：每个气球需要射出一支箭，总共需要4支箭。
#
# 示例 3：
#
#
# 输入：points = [[1,2],[2,3],[3,4],[4,5]]
# 输出：2
# 解释：气球可以用2支箭来爆破:
# - 在x = 2处发射箭，击破气球[1,2]和[2,3]。
# - 在x = 4处射出箭，击破气球[3,4]和[4,5]。
#
#
#
#
#
# 提示:
#
#
# 1 <= points.length <= 10^5
# points[i].length == 2
# -2^31 <= xstart < xend <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 局部最优解：当气球区间出现重叠的时候，一起射，使用弓箭最少
        # 全局最优：将所有气球射爆使用弓箭最少
        # 先按照起始位置排序，遍历气球数组，每两个比较求解公共区间，若是有公共区间，用更新后的公共区间与下一个气球区间作比较，继续遍历，否则弓箭数加一
        points = sorted(points, key=lambda x: x[-1])
        arrow = 1
        cur_index = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > cur_index:
                arrow += 1
                cur_index = points[i][1]
        return arrow
        # @lc code=end
