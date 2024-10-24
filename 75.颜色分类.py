#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#
# https://leetcode.cn/problems/sort-colors/description/
#
# algorithms
# Medium (60.30%)
# Likes:    1840
# Dislikes: 0
# Total Accepted:    694.1K
# Total Submissions: 1.1M
# Testcase Example:  '[2,0,2,1,1,0]'
#
# 给定一个包含红色、白色和蓝色、共 n 个元素的数组 nums ，原地 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
#
# 我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
#
#
#
# 必须在不使用库内置的 sort 函数的情况下解决这个问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,0,2,1,1,0]
# 输出：[0,0,1,1,2,2]
#
#
# 示例 2：
#
#
# 输入：nums = [2,0,1]
# 输出：[0,1,2]
#
#
#
#
# 提示：
#
#
# n == nums.length
# 1 <= n <= 300
# nums[i] 为 0、1 或 2
#
#
#
#
# 进阶：
#
#
# 你能想出一个仅使用常数空间的一趟扫描算法吗？
#
#
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 把0和1交换到头端，前者交换0，后者交换1
        count_0 = 0
        count_1 = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                # 1先交换到头部
                nums[count_1], nums[i] = nums[i], nums[count_1]
                count_1 += 1
            elif nums[i] == 0:
                # 为0的情况，这时候先把0交换到头部，这里可能把1交换出来的，再把1交换到当前的末尾去，同时更新0和1的指针
                nums[count_0], nums[i] = nums[i], nums[count_0]
                if count_0 < count_1:
                    # 把1拿回来，再进行两边的更新
                    nums[count_1], nums[i] = nums[i], nums[count_1]
                count_0 += 1
                count_1 += 1
        # 更简单的实现是左边交换0，右边交换2

# @lc code=end
