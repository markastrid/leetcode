#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (57.03%)
# Likes:    1174
# Dislikes: 0
# Total Accepted:    547K
# Total Submissions: 942.8K
# Testcase Example:  '[3,4,5,1,2]'
#
# 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7]
# 在变化后可能得到：
#
# 若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
# 若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
#
#
# 注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2],
# ..., a[n-2]] 。
#
# 给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。
#
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [3,4,5,1,2]
# 输出：1
# 解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2]
# 输出：0
# 解释：原数组为 [0,1,2,4,5,6,7] ，旋转 3 次得到输入数组。
#
#
# 示例 3：
#
#
# 输入：nums = [11,13,15,17]
# 输出：11
# 解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# nums 中的所有整数 互不相同
# nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
#
#
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 旋转后的数组一定被分成了前后两部分且两半都是升序数组，且前一半的最小值一定大于后一半的最大值，只要用二分找到后一半的第一个元素即可
        left = 0
        right = len(nums)-1
        min_num = nums[0]
        while left <= right:
            middle = (left+right)//2
            if nums[middle] < min_num:
                # 如果中间位置比min小，那么这个mid位置一定在第二段升序数组中，那么最小值一定在mid或者它的左边，这是因为每段都是升序的
                min_num = nums[middle]
                right = middle-1
            else:
                left = middle+1
        return min_num


# @lc code=end
