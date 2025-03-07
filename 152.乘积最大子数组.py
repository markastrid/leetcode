#
# @lc app=leetcode.cn id=152 lang=python3
#
# [152] 乘积最大子数组
#
# https://leetcode.cn/problems/maximum-product-subarray/description/
#
# algorithms
# Medium (43.08%)
# Likes:    2332
# Dislikes: 0
# Total Accepted:    485.7K
# Total Submissions: 1.2M
# Testcase Example:  '[2,3,-2,4]'
#
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 
# 测试用例的答案是一个 32-位 整数。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: nums = [2,3,-2,4]
# 输出: 6
# 解释: 子数组 [2,3] 有最大乘积 6。
# 
# 
# 示例 2:
# 
# 
# 输入: nums = [-2,0,-1]
# 输出: 0
# 解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
# 
# 
# 
# 提示:
# 
# 
# 1 <= nums.length <= 2 * 10^4
# -10 <= nums[i] <= 10
# nums 的任何子数组的乘积都 保证 是一个 32-位 整数
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return None
        max_ans=1
        min_ans=1
        ans=nums[0]
        for i in range(len(nums)):
            #负值：max与min进行交换再进行下一步计算
            if nums[i]<0:
                max_ans,min_ans=min_ans,max_ans
            max_ans=max(max_ans*nums[i],nums[i])
            min_ans=min(min_ans*nums[i],nums[i])
            ans=max(max_ans,ans)
        return ans
            
# @lc code=end

