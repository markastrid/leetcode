#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#
# https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array/description/
#
# algorithms
# Medium (42.40%)
# Likes:    2810
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '[5,7,7,8,8,10]\n8'
#
# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
# 如果数组中不存在目标值 target，返回 [-1, -1]。
#
# 你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
# 示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
# 示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# nums 是一个非递减数组
# -10^9 <= target <= 10^9
#
#
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 二分查找的变体：找到头和尾巴,第一个等于的和最后一个等于的,这样会好处理一点
        left = 0
        right = len(nums)-1
        first = -1
        last = -1
        while left <= right:
            mid = (left+right)//2
            # 这里把nums[mid] == target and mid == 0放在前面能够防止下标溢出
            if (nums[mid] == target and mid == 0) or (nums[mid] == target and nums[mid-1] < target):
                first = mid
                break
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if (nums[mid] == target and mid == len(nums)-1) or (nums[mid] == target and nums[mid+1] > target):
                last = mid
                break
            if nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
        return [first, last]
        # @lc code=end
