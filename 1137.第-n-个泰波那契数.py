#
# @lc app=leetcode.cn id=1137 lang=python3
#
# [1137] 第 N 个泰波那契数
#
# https://leetcode.cn/problems/n-th-tribonacci-number/description/
#
# algorithms
# Easy (60.97%)
# Likes:    317
# Dislikes: 0
# Total Accepted:    224.3K
# Total Submissions: 367.6K
# Testcase Example:  '4'
#
# 泰波那契序列 Tn 定义如下： 
#
# T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
#
# 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。
#
#
#
# 示例 1：
#
# 输入：n = 4
# 输出：4
# 解释：
# T_3 = 0 + 1 + 1 = 2
# T_4 = 1 + 1 + 2 = 4
#
#
# 示例 2：
#
# 输入：n = 25
# 输出：1389537
#
#
#
#
# 提示：
#
#
# 0 <= n <= 37
# 答案保证是一个 32 位整数，即 answer <= 2^31 - 1。
#
#
#

# @lc code=start
class Solution:
    def tribonacci(self, n: int) -> int:
        # 递归最简单，但是容易超时
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        t_0 = 0
        t_1 = 1
        t_2 = 1
        temp = -1
        for i in range(3, n+1):
            temp = t_0+t_1+t_2
            t_0, t_1, t_2 = t_1, t_2, temp
        return temp
        # @lc code=end
