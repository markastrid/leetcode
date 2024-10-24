#
# @lc app=leetcode.cn id=31 lang=python3
#
# [31] 下一个排列
#
# https://leetcode.cn/problems/next-permutation/description/
#
# algorithms
# Medium (38.17%)
# Likes:    2586
# Dislikes: 0
# Total Accepted:    565.7K
# Total Submissions: 1.4M
# Testcase Example:  '[1,2,3]'
#
# 整数数组的一个 排列  就是将其所有成员以序列或线性顺序排列。
#
#
# 例如，arr = [1,2,3] ，以下这些都可以视作 arr 的排列：[1,2,3]、[1,3,2]、[3,1,2]、[2,3,1] 。
#
#
# 整数数组的 下一个排列 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 下一个排列
# 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
#
#
# 例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
# 类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
# 而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。
#
#
# 给你一个整数数组 nums ，找出 nums 的下一个排列。
#
# 必须 原地 修改，只允许使用额外常数空间。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,2,3]
# 输出：[1,3,2]
#
#
# 示例 2：
#
#
# 输入：nums = [3,2,1]
# 输出：[1,2,3]
#
#
# 示例 3：
#
#
# 输入：nums = [1,1,5]
# 输出：[1,5,1]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 100
#
#
#

# @lc code=start
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 必须原地修改，只允许使用额外常数空间
        # “下一个排列” 的定义是：给定数字序列的字典序中下一个更大的排列。如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
        # 通过教程得到的分析：
        # 1.我们需要将后面的大数与前面的小数交换
        # 2.交换之后增加的幅度尽可能小：逆序查找；交换的大数要尽可能小；交换完大数后面需要重置为升序
        # 要让数字变大，就可以将原本在靠右侧的大数和比起较小且在其左侧的数交换位置。
        # 现在求变大幅度最小的数，那么交换的数就应该尽可能地发生在靠右侧，所以从右向左找可以交换数来实现数变大的区间，因为一组数按降序排就已经是最小的，所以如果当前区间的数已经是降序排列就无法再通过交换数实现数变大，因此已知从右向左扩大区间直到找到区间不再满足降序，也就是找到第一个nums[i] < nums[i + 1]
        # 这时候这个区间就是可以通过交换数变得更大：在nums[i + 1: end]范围内找一个比nums[i]大的数和nums[i]交换，同时为了让增幅最小，要选择nums[i + 1: end]中比nums[i]大的数中最小的数和nums[i]交换即可，因为已知nums[i + 1: end]是降序排列，因此只需要从右向左遍历nums[i + 1: end]找到第一个比nums[i]大的数和nums[i]交换即可（因为已知nums[i + 1] ＞ nums[i]所以nums[i + 1: end]中一定存在＞nums[i]的数）。交换之后nums[i + 1: end]仍然为降序（因为是在有序序列中找到第一个比nums[i]大的数，就说明之前都比其小，之后都比其大，交换后仍然满足降序），反转其为升序使得其变得最小
        exchange = False
        for i in range(len(nums)-2, -1, -1):
            if exchange:
                break
            if nums[i] < nums[i+1]:
                exchange = True
                min = nums[i+1]
                min_index = i+1
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j] and nums[j] <= min:
                        min = nums[j]
                        min_index = j
                nums[min_index] = nums[i]
                nums[i] = min
                nums[i + 1:] = reversed(nums[i + 1:])
        if not exchange:
            nums.reverse()

            # @lc code=end
