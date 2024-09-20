# @lcpr-before-debug-begin
from python3problem1 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=1 lang=python3
# @lcpr version=30116
#
# [1] 两数之和
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
      for i in range(len(nums)):
        res=target-nums[i]
        if res in nums[i+1:]:
          return [i,nums[i+1:].index(res)+i+1]
# @lc code=end



#
# @lcpr case=start
# [2,7,11,15]\n9\n
# @lcpr case=end

# @lcpr case=start
# [3,2,4]\n6\n
# @lcpr case=end

# @lcpr case=start
# [3,3]\n6\n
# @lcpr case=end

#

