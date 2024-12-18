#
# @lc app=leetcode.cn id=665 lang=python3
#
# [665] 非递减数列
#
# https://leetcode.cn/problems/non-decreasing-array/description/
#
# algorithms
# Medium (27.67%)
# Likes:    797
# Dislikes: 0
# Total Accepted:    114.1K
# Total Submissions: 407.2K
# Testcase Example:  '[4,2,3]'
#
# 给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
#
# 我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
#
#
#
# 示例 1:
#
#
# 输入: nums = [4,2,3]
# 输出: true
# 解释: 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。
#
#
# 示例 2:
#
#
# 输入: nums = [4,2,1]
# 输出: false
# 解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
#
#
#
#
# 提示：
#
#
#
# n == nums.length
# 1 <= n <= 10^4
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # 两次遍历：第一次找到非递减的那个数，修改掉它(在能修改的情况下);第二次遍历观察是否为非递减数组
        # 是否能修改,这里相当于对0->1做判断了
        # 0<1的话这里就需要修改一次，后面就不能修改了；否则不需要修改
        if len(nums) == 1:
            return True
        count = True if nums[0] <= nums[1] else False
        for i in range(1, len(nums)-1):
            # 找到违反的对
            if nums[i] > nums[i+1]:
                if count:
                    if nums[i+1] >= nums[i-1]:
                        nums[i] = nums[i+1]
                    else:
                        nums[i+1] = nums[i]
                    count = False
                else:
                    return False
        return True

        # @lc code=end
