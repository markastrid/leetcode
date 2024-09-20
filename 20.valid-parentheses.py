#
# @lc app=leetcode.cn id=20 lang=python3
# @lcpr version=30117
#
# [20] 有效的括号
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
      dic={")":"(","]":"[","}":"{"}
      stack=[]#栈
      for i in s:
        if stack and i in dic:  
          if dic[i]==stack[-1]:#stack[-1]表示上一个栈中最后一个元素
            stack.pop()
          else:
            return False
        else:
          stack.append(i)
      return  not stack  
        
        
          
        
# @lc code=end



#
# @lcpr case=start
# "()"\n
# @lcpr case=end

# @lcpr case=start
# "()[]{}"\n
# @lcpr case=end

# @lcpr case=start
# "(]"\n
# @lcpr case=end

#

