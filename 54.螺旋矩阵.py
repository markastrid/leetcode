#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode.cn/problems/spiral-matrix/description/
#
# algorithms
# Medium (49.28%)
# Likes:    1777
# Dislikes: 0
# Total Accepted:    612.4K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
#
#
#
# 示例 1：
#
#
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
#
# 示例 2：
#
#
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#
#
# 提示：
#
#
# m == matrix.length
# n == matrix[i].length
# 1
# -100
#
#
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        length = len(matrix[0])
        width = len(matrix)
        left, right, up, down = 0, length-1,  width-1, 0
        ans = []
        while True:
            for i in range(left, right+1):
                ans.append(matrix[down][i])
            down += 1
            if down > up:
                break
            for i in range(down, up+1):
                ans.append(matrix[i][right])
            right -= 1
            if right < left:
                break
            for i in range(right, left-1, -1):
                ans.append(matrix[up][i])
            up -= 1
            if up < down:
                break
            for i in range(up, down-1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break
        return ans

# @lc code=end
