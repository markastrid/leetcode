#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode.cn/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (64.10%)
# Likes:    2631
# Dislikes: 0
# Total Accepted:    1.2M
# Total Submissions: 2M
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。
#
# 请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
#
# 你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1:
#
#
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#
#
# 示例 2:
#
#
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4
#
#
#
# 提示：
#
#
# 1 <= k <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # O(n)的算法，可以使用快速排序的思想
        # 快速排序的思想是，每次选择一个基准元素，将比基准元素小的元素放在左边，比基准元素大的元素放在右边
        # 然后判断基准元素的位置，如果基准元素的位置等于k-1，那么基准元素就是第k大的元素
        # 如果基准元素的位置小于k-1，那么第k大的元素在基准元素的右边，如果基准元素的位置大于k-1，那么第k大的元素在基准元素的左边
        # 这样就可以减少排序的次数
        def quick_sort(nums, left, right):
            if left < right:
                pivot = partition(nums, left, right)
                if pivot == k - 1:
                    return nums[pivot]
                elif pivot < k - 1:
                    return quick_sort(nums, pivot + 1, right)
                else:
                    return quick_sort(nums, left, pivot - 1)
            return nums[k - 1]
        #partition函数，将比基准元素小的元素放在左边，比基准元素大的元素放在右边
        # 返回基准元素的位置
        def partition(nums, left, right):
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] <= pivot:
                    right -= 1
                nums[left],nums[right] = nums[right],nums[left]
                while left < right and nums[left] >= pivot:
                    left += 1
                nums[right],nums[left] = nums[left],nums[right]
            nums[left] = pivot
            return left
        return quick_sort(nums, 0, len(nums) - 1)
# @lc code=end
