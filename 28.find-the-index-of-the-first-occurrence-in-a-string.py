#
# @lc app=leetcode.cn id=28 lang=python3
# @lcpr version=30119
#
# [28] 找出字符串中第一个匹配项的下标
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
     """
    for i in range(len(haystack)):
        start=i
        length=0
        count=i
        for j in range(len(needle)):
          if count>=len(haystack):
            return -1
          if haystack[count]==needle[j]:
            length+=1
            count+=1
          if length==len(needle):
            return start
      return -1 
      """
     return haystack.find(needle)
# @lc code=end



#
# @lcpr case=start
# "sadbutsad"\n"sad"\n
# @lcpr case=end

# @lcpr case=start
# "leetcode"\n"leeto"\n
# @lcpr case=end

#

