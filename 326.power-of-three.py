#
# @lc app=leetcode.cn id=326 lang=python3
# @lcpr version=30119
#
# [326] 3 的幂
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      while (n>1):
        n=n/3
      if n==1:
        return True
      return False
      
# @lc code=end



#
# @lcpr case=start
# 27\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

# @lcpr case=start
# 9\n
# @lcpr case=end

# @lcpr case=start
# 45\n
# @lcpr case=end

#

