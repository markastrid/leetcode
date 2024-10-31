#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode.cn/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (55.11%)
# Likes:    2250
# Dislikes: 0
# Total Accepted:    808.4K
# Total Submissions: 1.6M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
#
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
#
#
#
# 示例 1：
#
#
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
#
# 示例 2：
#
#
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
#
#
#
#
# 提示：
#
#
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
#
#
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        # 这里是log n的处理方法
        max_len = 1
        length = 1
        # nums.sort()会在原地排序，不会返回值给这个结果，因此想要返回值要用sorted
        nums = sorted(list(set(nums)))
        # 注意排序放在最后一步，貌似set()过程不稳定，会破坏原有的数组顺序
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]+1:
                length += 1
                max_len = max(length, max_len)
            else:
                length = 1
        return max_len 
        '''

        # n的处理方法
        hash_set = set(nums)
        count = 1
        max_length = 0
        for i in hash_set:
            if i-1 in hash_set:
                continue
            current = i
            count = 1
            while current+1 in hash_set:
                current += 1
                count += 1
            max_length = max(max_length, count)
        return max_length

# @lc code=end
