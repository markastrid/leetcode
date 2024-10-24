#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#
# https://leetcode.cn/problems/3sum/description/
#
# algorithms
# Medium (36.63%)
# Likes:    7090
# Dislikes: 0
# Total Accepted:    2M
# Total Submissions: 5.2M
# Testcase Example:  '[-1,0,1,2,-1,-4]'
#
# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j !=
# k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
#
#
#
#
# 示例 1：
#
#
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。
#
#
# 示例 2：
#
#
# 输入：nums = [0,1,1]
# 输出：[]
# 解释：唯一可能的三元组和不为 0 。
#
#
# 示例 3：
#
#
# 输入：nums = [0,0,0]
# 输出：[[0,0,0]]
# 解释：唯一可能的三元组和为 0 。
#
#
#
#
# 提示：
#
#
# 3 <= nums.length <= 3000
# -10^5 <= nums[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        # 先想到的办法果然是三重数组，这样时间会超限
        # 答案数组
        ans = []
        nums = sorted(nums)
        for i in range(len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    # target = 0-nums[i]
                    if nums[i]+nums[j]+nums[k] == 0:
                        ans.append([nums[i], nums[j], nums[k]])
        # 注意python里拷贝要用深层拷贝，不然是会指向同一个数组，没变化
        new_ans = copy.deepcopy(ans)
        # print(new_ans)
        # print(ans)
        for i in range(len(ans)-1):
            for j in range(i+1, len(ans)):
                if ans[i] == ans[j]:
                    # remove只能删除第一个指定元素
                    new_ans.remove(ans[i])
                    # break保证我们只删除一个元素一次，不会删除完
                    break
        return new_ans
        '''
        # 「双指针」，当我们需要枚举数组中的两个元素时，如果我们发现随着第一个元素的递增，第二个元素是递减的，那么就可以使用双指针的方法，将枚举的时间复杂度从 O(N2) 减少至 O(N)
        # 先从小到大排序
        nums.sort()
        ans = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                continue
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    #先把这个正确的加上
                    ans.append([nums[i], nums[left], nums[right]])
                    #通过循环把后面所有的重复全部删除
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans
        # @lc code=end
