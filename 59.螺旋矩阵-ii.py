#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode.cn/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (74.37%)
# Likes:    1343
# Dislikes: 0
# Total Accepted:    472.6K
# Total Submissions: 668.5K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
#
#
#
# 示例 1：
#
#
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#
#
# 示例 2：
#
#
# 输入：n = 1
# 输出：[[1]]
#
#
#
#
# 提示：
#
#
# 1
#
#
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        left, right, down, up = 0, n-1, 0, n-1
        while count <= n*n:
            for i in range(left, right+1):
                ans[down][i] = count
                count += 1
            down += 1
            # if down > up:
            #    break
            for i in range(down, up+1):
                ans[i][right] = count
                count += 1
            right -= 1
            # if right < left:
            #    break
            for i in range(right, left-1, -1):
                ans[up][i] = count
                count += 1
            up -= 1
            # if up < down:
            #    break
            for i in range(up, down-1, -1):
                ans[i][left] = count
                count += 1
            left += 1
            # if left > right:
            #    break
        return ans
        # 这里跟[54]的解法不同在于，前者的默认循环是true的，而后者可以通过直接加减来走出循环，因此不需要边界条件，而前者不行

# @lc code=end
