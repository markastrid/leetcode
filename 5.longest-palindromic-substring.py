#
# @lc app=leetcode.cn id=5 lang=python3
# @lcpr version=30117
#
# [5] 最长回文子串
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def expand(self,left,right,s):
      while left>=0 and right<=len(s)-1 and s[left]==s[right]:
        left-=1
        right+=1
      return left+1,right-1
    def longestPalindrome(self, s: str) -> str:
      start=0
      end=0
      for i in range(len(s)-1):
        left1,right1=self.expand(i,i,s)
        left2,right2=self.expand(i,i+1,s)
        if right1-left1>end-start:
          start,end=left1,right1
        if right2-left2>end-start:
          start,end=left2,right2
      return s[start:end+1]

# @lc code=end



#
# @lcpr case=start
# "babad"\n
# @lcpr case=end

# @lcpr case=start
# "cbbd"\n
# @lcpr case=end

#

