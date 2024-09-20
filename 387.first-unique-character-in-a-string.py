#
# @lc app=leetcode.cn id=387 lang=python3
# @lcpr version=30121
#
# [387] 字符串中的第一个唯一字符
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
      '''
      方法一:用列表把每个字母出现的频率记下来，然后
      第二次遍历找到第一个只出现一次的字母，返回；
      没找到就返回-1
      '''
      record=[0]*26
      for i in s:
        record[ord(i)-ord('a')]+=1
      for i in range(len(s)):
        if record[ord(s[i])-ord('a')]==1:
          return i
      return -1
   
# @lc code=end



#
# @lcpr case=start
# "leetcode"\n
# @lcpr case=end

# @lcpr case=start
# "loveleetcode"\n
# @lcpr case=end

# @lcpr case=start
# "aabb"\n
# @lcpr case=end

#

