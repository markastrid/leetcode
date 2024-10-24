#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#
# https://leetcode.cn/problems/set-matrix-zeroes/description/
#
# algorithms
# Medium (62.69%)
# Likes:    1111
# Dislikes: 0
# Total Accepted:    443K
# Total Submissions: 646.2K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]
#
#
# 示例 2：
#
#
# 输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# 输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -2^31 <= matrix[i][j] <= 2^31 - 1
#
#
#
#
# 进阶：
#
#
# 一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
# 一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
# 你能想出一个仅使用常量空间的解决方案吗？
#
#
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
       # O(m∗n) 和 O(m+n) 空间的解法都十分简单：「同等大小的矩阵」或「与行列数量相等的标识」来记录置零信息
       # 用首行和首列来判断是否需要置0：因为如果某行\列需要置零那么首行对应元素一定置零
       # 用两个额外常数空间判断首行首列是否需要置零
       # 默认1表示不需要置零
        column = 1
        row = 1
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            if matrix[0][i] == 0:
                row = 0
        for i in range(m):
            if matrix[i][0] == 0:
                column = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if column == 0:
            for i in range(m):
                matrix[i][0] = 0
        if row == 0:
            for i in range(n):
                matrix[0][i] = 0
            # @lc code=end
