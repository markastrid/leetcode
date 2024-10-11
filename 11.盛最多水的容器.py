#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#
# https://leetcode.cn/problems/container-with-most-water/description/
#
# algorithms
# Medium (60.67%)
# Likes:    5137
# Dislikes: 0
# Total Accepted:    1.4M
# Total Submissions: 2.4M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
#
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
#
# 返回容器可以储存的最大水量。
#
# 说明：你不能倾斜容器。
#
#
#
# 示例 1：
#
#
#
#
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49
# 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
#
# 示例 2：
#
#
# 输入：height = [1,1]
# 输出：1
#
#
#
#
# 提示：
#
#
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 解析这个问题：即两个点之间的距离和两个点最小的那个高度组成的长方形的面积最大
        left = 0
        right = len(height)-1
        max_square = 0
        # 双指针没有问题，但是移动条件是较小的那个先移动

        def square(height, left, right):
            return min(height[left], height[right])*(right-left)
        while left < right:
            max_square = max(max_square, square(height, left, right))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_square
        # @lc code=end
