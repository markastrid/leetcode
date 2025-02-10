#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#
# https://leetcode.cn/problems/search-in-rotated-sorted-array-ii/description/
#
# algorithms
# Medium (41.13%)
# Likes:    797
# Dislikes: 0
# Total Accepted:    232.1K
# Total Submissions: 565.5K
# Testcase Example:  '[2,5,6,0,0,1,2]\n0'
#
# 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。
#
# 在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k],
# nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始
# 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。
#
# 给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值
# target ，则返回 true ，否则返回 false 。
#
# 你必须尽可能减少整个操作步骤。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,5,6,0,0,1,2], target = 0
# 输出：true
#
#
# 示例 2：
#
#
# 输入：nums = [2,5,6,0,0,1,2], target = 3
# 输出：false
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# 题目数据保证 nums 在预先未知的某个下标上进行了旋转
# -10^4 <= target <= 10^4
#
#
#
#
# 进阶：
#
#
# 此题与 搜索旋转排序数组 相似，但本题中的 nums  可能包含 重复 元素。这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
#
#
#
#
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # 在33基础上进行进一步判断
        # 对于数组中有重复元素的情况，二分查找时可能会有 a[l]=a[mid]=a[r]，此时无法判断区间 [l,mid] 和区间 [mid+1,r] 哪个是有序的。
        # 对于这种情况，我们只能将当前二分区间的左边界加一，右边界减一，然后在新区间上继续二分查找。
        left = 0
        right = len(nums)-1
        while left <= right:
            middle = (left+right)//2
            if nums[middle] == target:
                return True
            if nums[left] == nums[middle]:
                left += 1
                continue
            # nums[left] == nums[middle]的情况，这时候两边都是有序的，相当于划分点为nums[left]这个值，这是可以确定的
            # 但是三个都相等的时候我们不知道划分点在左边还是右边，例如[3,3,3,3,3,1,2,3,3]
            # 分left与middle大小情况讨论：三种情况，分属于不同的区间和判断
            # right和middle也类似
            if nums[left] < nums[middle]:
                if nums[left] <= target <= nums[middle]:
                    right = middle-1
                else:
                    left = middle+1
            else:
                if nums[middle] <= target <= nums[right]:
                    left = middle+1
                else:
                    right = middle-1
        return False

        # @lc code=end
