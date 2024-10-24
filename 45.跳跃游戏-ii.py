#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# https://leetcode.cn/problems/jump-game-ii/description/
#
# algorithms
# Medium (45.19%)
# Likes:    2622
# Dislikes: 0
# Total Accepted:    808.9K
# Total Submissions: 1.8M
# Testcase Example:  '[2,3,1,1,4]'
#
# 给定一个长度为 n 的 0 索引整数数组 nums。初始位置为 nums[0]。
#
# 每个元素 nums[i] 表示从索引 i 向前跳转的最大长度。换句话说，如果你在 nums[i] 处，你可以跳转到任意 nums[i + j]
# 处:
#
#
# 0 <= j <= nums[i] 
# i + j < n
#
#
# 返回到达 nums[n - 1] 的最小跳跃次数。生成的测试用例可以到达 nums[n - 1]。
#
#
#
# 示例 1:
#
#
# 输入: nums = [2,3,1,1,4]
# 输出: 2
# 解释: 跳到最后一个位置的最小跳跃数是 2。
# 从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
#
#
# 示例 2:
#
#
# 输入: nums = [2,3,0,1,4]
# 输出: 2
#
#
#
#
# 提示:
#
#
# 1 <= nums.length <= 10^4
# 0 <= nums[i] <= 1000
# 题目保证可以到达 nums[n-1]
#
#
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        # we set count for the times of jumping
        count = 0
        n = len(nums)
        distance = 0
        max_distance = 0
        # 我们采用力扣的第二个方法，正向的依次选取：
        # 首先选择从下标0所在位置能够到达的所有位置，选择其中能到达最远位置的下标作为第一步，也就是当前的最大距离，接着从该下标到其到达的最远位置之间中选择下一步能够到达的最远位置为第二步；
        # 以此类推
        # 这是因为，举例来说，如果我们到达最后一步，说明前面只有我们选择的这步能够直接到达最后的点，其他的步骤都会在中途停下才能再走一步，至少会多出来一步
        # 以此类推
        # 这里的max_distance和distance有点像第二步的位置和第一步的位置(对当前来说)
        # max_distance是当前我们需要找到的第一步内的最长的第二步，当到达边界的时候我们就将其更新为下一个边界，并且让步骤+1
        # 或者说distance其实就是当前棋子所在的地方
        for i in range(n-1):
            # 第一个边界
            max_distance = max(max_distance, i+nums[i])
            if i == distance:
                distance = max_distance
                count += 1
        return count
        # @lc code=end
