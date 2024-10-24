#
# @lc app=leetcode.cn id=18 lang=python3
#
# [18] 四数之和
#
# https://leetcode.cn/problems/4sum/description/
#
# algorithms
# Medium (37.60%)
# Likes:    1974
# Dislikes: 0
# Total Accepted:    632.2K
# Total Submissions: 1.7M
# Testcase Example:  '[1,0,-1,0,-2,2]\n0'
#
# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
# nums[b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
#
#
# 0 <= a, b, c, d < n
# a、b、c 和 d 互不相同
# nums[a] + nums[b] + nums[c] + nums[d] == target
#
#
# 你可以按 任意顺序 返回答案 。
#
#
#
# 示例 1：
#
#
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
#
# 示例 2：
#
#
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#
#
#
#
# 提示：
#
#
# 1 <= nums.length <= 200
# -10^9 <= nums[i] <= 10^9
# -10^9 <= target <= 10^9
#
#
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        # ans = {}
        # 双层指针
        # 注意本题是abcd四个下标都互不相同且不能出现完全重复，不是本身不能重复
        # 因此我的去重是使用字典，而循环是采取的类似前面的三重思想，已经注释掉字典方法了
        # 上网搜了一下，这里的方法基本相同，优化的手段主要在于剪枝(剪枝从零可以打败极大部分人)，这里根据此思想修改代码
        # 我采用的是使用字典进行去重，因此效果较差
        for i in range(len(nums)-3):
            # 去重操作，此题不需要
            # if i+1 < len(nums) and nums[i+1] == nums[i]:
            # continue
            x = nums[i]
            # 跳过重复数字,这里选择跳后面的数字，就不会产生全部相同的数字没有被纳入考虑的情况，如[-1,-1,0,2]这样的
            if i and x == nums[i - 1]:
                continue
            if x + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:  # 优化一
                break
            if x + nums[-3] + nums[-2] + nums[-1] < target:  # 优化二
                continue
            for j in range(i+1, len(nums)-2):
                # 去重操作，此题不需要
                # if j+1 < len(nums) and nums[j+1] == nums[j]:
                # continue
                y = nums[j]
                if j > i + 1 and y == nums[j - 1]:  # 跳过重复数字
                    continue
                if x + y + nums[j + 1] + nums[j + 2] > target:  # 优化一
                    break
                if x + y + nums[-2] + nums[-1] < target:  # 优化二
                    continue
                left = j+1
                right = len(nums)-1
                while left < right:
                    # 去重操作，此题不需要
                    # while left < right and nums[left] == nums[left+1]:
                    # left += 1
                    # while left < right and nums[right] == nums[right-1]:
                    # right -= 1
                    sum = nums[i]+nums[left]+nums[j]+nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:  # 跳过重复数字
                            left += 1
                        # 跳过重复数字
                        right -= 1
                        while right > left and nums[right] == nums[right + 1]:
                            right -= 1
                        # 上面这两次去重，同样的先纳入计算，在下一次的时候对前面的进行去重，这样能防止出现像示例1情况下，[-2,0,0,2]这样的有重复数字的答案不被纳入考虑的情况,这里的两个left\right加减都是很有说法的，考虑不到的时候可以直接采用我的字典去重方式，最后一个循环优化的计算量已经几乎没有了
        # list_ans = []
        # for key in ans:
            # list_ans.append(list(key))
        return ans


# @lc code=end
