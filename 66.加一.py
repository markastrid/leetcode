#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode.cn/problems/plus-one/description/
#
# algorithms
# Easy (45.44%)
# Likes:    1433
# Dislikes: 0
# Total Accepted:    784.6K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3]'
#
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
#
#
# 示例 1：
#
#
# 输入：digits = [1,2,3]
# 输出：[1,2,4]
# 解释：输入数组表示数字 123。
#
#
# 示例 2：
#
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
#
#
# 示例 3：
#
#
# 输入：digits = [0]
# 输出：[1]
#
#
#
#
# 提示：
#
#
# 1
# 0
#
#
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)-1
        digits[length] += 1
        while length > 0:
            if digits[length] <= 9:
                break
            else:
                digits[length] = 0
                digits[length-1] += 1
            length -= 1
        if digits[0] == 10:
            digits[0] = 0
            digits.insert(0, 1)
        return digits

# @lc code=end
