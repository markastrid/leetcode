#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#
# https://leetcode.cn/problems/sqrtx/description/
#
# algorithms
# Easy (38.69%)
# Likes:    1607
# Dislikes: 0
# Total Accepted:    985.1K
# Total Submissions: 2.5M
# Testcase Example:  '4'
#
# 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。
#
# 由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。
#
# 注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。
#
#
#
# 示例 1：
#
#
# 输入：x = 4
# 输出：2
#
#
# 示例 2：
#
#
# 输入：x = 8
# 输出：2
# 解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。
#
#
#
#
# 提示：
#
#
# 0 <= x <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        # 0会产生除0的情况，因此这里额外考虑
        if x == 0:
            return 0
        l = 1
        r = x
        while l <= r:
            middle = int((r+l)/2)
            ans = int(x/middle)
            if middle == ans:
                return ans
            elif middle < ans:
                l = middle+1
            else:
                r = middle-1
        return r
        '''
        # 牛顿迭代法算平方根：Xn+1=Xn-f(n)/f'(n)
        a = x
        while a*a > x:
            a = int((a+x/a)/2)
        return a

# @lc code=end
