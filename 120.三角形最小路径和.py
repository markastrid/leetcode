#
# @lc app=leetcode.cn id=120 lang=python3
#
# [120] 三角形最小路径和
#
# https://leetcode.cn/problems/triangle/description/
#
# algorithms
# Medium (68.72%)
# Likes:    1380
# Dislikes: 0
# Total Accepted:    380.2K
# Total Submissions: 550.7K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# 给定一个三角形 triangle ，找出自顶向下的最小路径和。
#
# 每一步只能移动到下一行中相邻的结点上。相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1
# 的两个结点。也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
#
#
#
# 示例 1：
#
#
# 输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# 输出：11
# 解释：如下面简图所示：
# ⁠  2
# ⁠ 3 4
# ⁠6 5 7
# 4 1 8 3
# 自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。
#
#
# 示例 2：
#
#
# 输入：triangle = [[-10]]
# 输出：-10
#
#
#
#
# 提示：
#
#
# 1
# triangle[0].length == 1
# triangle[i].length == triangle[i - 1].length + 1
# -10^4
#
#
#
#
# 进阶：
#
#
# 你可以只使用 O(n) 的额外空间（n 为三角形的总行数）来解决这个问题吗？
#
#
#

# @lc code=start
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # 这个就是用到杨辉三角的思想：下一层加上一层与自己相邻的两个节点中的较小者，依次类推，最后找到倒数第一层的最小节点
        num = len(triangle)
        i = 1
        # 第一层
        ans = [triangle[0]]
        # 从第二层刀最后一层
        for i in range(1, num):
            # 当前层左边
            single = [ans[i-1][0]+triangle[i][0]]
            j = 1
            # 当前层中间，用ans+triangle是为了保证最后的结果是路径和，不重不漏
            while j < i:
                single.append(
                    min(ans[i-1][j-1], ans[i-1][j])+triangle[i][j])
                j += 1
            # 当前层右边
            single.append(ans[i-1][i-1]+triangle[i][i])
            ans.append(single)
        return min(ans[-1])
# @lc code=end
