#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#
# https://leetcode.cn/problems/sum-of-square-numbers/description/
#
# algorithms
# Medium (38.52%)
# Likes:    494
# Dislikes: 0
# Total Accepted:    165.7K
# Total Submissions: 429.4K
# Testcase Example:  '5'
#
# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a^2 + b^2 = c 。
#
#
#
# 示例 1：
#
#
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#
#
# 示例 2：
#
#
# 输入：c = 3
# 输出：false
#
#
#
#
# 提示：
#
#
# 0 <= c <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        # 用int(target**(0.5))**2 == target判断
        if c == 0:
            return True
        for i in range(1, int(c**(0.5))+1):
            target = c-i*i
            if int(target**(0.5))**2 == target:
                return True
        return False
        '''
        # 双指针判断
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            if left**2+right**2 == c:
                return True
            elif left**2+right**2 < c:
                left += 1
            else:
                right -= 1
        return False

# @lc code=end
