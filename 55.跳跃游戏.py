#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
# https://leetcode.cn/problems/jump-game/description/
#
# algorithms
# Medium (43.70%)
# Likes:    2875
# Dislikes: 0
# Total Accepted:    1.1M
# Total Submissions: 2.5M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给你一个非负整数数组 nums ，你最初位于数组的 第一个下标 。数组中的每个元素代表你在该位置可以跳跃的最大长度。
#
# 判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [2,3,1,1,4]
# 输出：true
# 解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
#
#
# 示例 2：
#
#
# 输入：nums = [3,2,1,0,4]
# 输出：false
# 解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 10^5
#
#
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        distance = 0
        max_distance = 0
        # 到n-1是因为默认一定能到边界，那么n-2的下标处就能触及到n-1的地方了，触及不到就是跑不到n-1
        n = len(nums)
        for i in range(n-1):
            max_distance = max(max_distance, nums[i]+i)
            if i == distance:
                # distance是当前确实能到达的最远边界
                distance = max_distance
        # 这里跟45题不同的是这里可以直接判断distance能不能到边界，一定有个地方是到不了边界的
        # 必须让distance作为判断条件，因为它是当前走的边界
        if distance >= n-1:
            return True
        return False

        # @lc code=end
