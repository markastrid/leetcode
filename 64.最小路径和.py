#
# @lc app=leetcode.cn id=64 lang=python3
#
# [64] 最小路径和
#
# https://leetcode.cn/problems/minimum-path-sum/description/
#
# algorithms
# Medium (69.45%)
# Likes:    1738
# Dislikes: 0
# Total Accepted:    677K
# Total Submissions: 951K
# Testcase Example:  '[[1,3,1],[1,5,1],[4,2,1]]'
#
# 给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
#
# 说明：每次只能向下或者向右移动一步。
#
#
#
# 示例 1：
#
#
# 输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
# 输出：7
# 解释：因为路径 1→3→1→1→1 的总和最小。
#
#
# 示例 2：
#
#
# 输入：grid = [[1,2,3],[4,5,6]]
# 输出：12
#
#
#
#
# 提示：
#
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200
#
#
#

# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        DP = [[0 for i in range(n+1)]for i in range(m+1)]
        DP[0][0] = grid[0][0]
        for i in range(1, n):
            DP[0][i] = DP[0][i-1]+grid[0][i]
        for i in range(1, m):
            DP[i][0] = DP[i-1][0]+grid[i][0]
        for i in range(1, m):
            for j in range(1, n):
                DP[i][j] = min(DP[i][j-1], DP[i-1][j])+grid[i][j]
        return DP[m-1][n-1]

        # @lc code=end
