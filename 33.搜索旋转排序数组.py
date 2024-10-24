#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode.cn/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (43.86%)
# Likes:    3034
# Dislikes: 0
# Total Accepted:    968.8K
# Total Submissions: 2.2M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
# 你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
# 示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
# 示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# nums 中的每个值都 独一无二
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
#
#
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 定理一：只有在顺序区间内才可以通过区间两端的数值判断target是否在其中。
        # 定理二：判断顺序区间还是乱序区间，只需要对比 left 和 right 是否是顺序对即可，left <= right，顺序区间，否则乱序区间。
        # 定理三：每次二分都会至少存在一个顺序区间。
        left = 0
        right = len(nums)-1
        while left <= right:
            index = (left+right)//2
            if nums[index] == target:
                return index
            if nums[left] <= nums[index]:
                if nums[left] <= target <= nums[index]:
                    right = index-1
                else:
                    left = index+1
            else:
                if nums[index] <= target <= nums[right]:
                    left = index+1
                else:
                    right = index-1
            # 为什么做+1/-1
            # 排除中间元素：因为我们已经比较过 mid 位置的元素了，所以不需要再次检查它
            # 保持搜索范围有效：通过将 right 更新为 mid - 1，确保下一次循环中 left 和 right 之间至少有一个元素，从而避免无限循环

        return -1
        # @lc code=end
