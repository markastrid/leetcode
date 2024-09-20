# @lcpr-before-debug-begin
from python3problem13 import *
from typing import *
# @lcpr-before-debug-end

#
# @lc app=leetcode.cn id=13 lang=python3
# @lcpr version=30117
#
# [13] 罗马数字转整数
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
  def romanToInt(self,s: str) -> int:
    list_Roman = list(s)
    sum = 0
    for i in range(len(s) - 1, -1, -1):
        if list_Roman[i] == 'I' and i < len(s)- 1 and list_Roman[i + 1] == 'V':
            sum -= 1
        elif list_Roman[i] == 'I' and i < len(s) - 1 and list_Roman[i + 1] == 'X':
            sum -= 1
        elif list_Roman[i] == 'I':
            sum += 1
        elif list_Roman[i] == 'X' and i < len(s) - 1 and list_Roman[i + 1] == 'L':
            sum = sum - 10
        elif list_Roman[i] == 'X' and i < len(s) - 1 and list_Roman[i + 1] == 'C':
            sum = sum - 10
        elif list_Roman[i] == 'X':
            sum += 10
        elif list_Roman[i] == 'C' and i < len(s) - 1 and list_Roman[i + 1] == 'D':
            sum = sum - 100
        elif list_Roman[i] == 'C' and i <len(s)- 1 and list_Roman[i + 1] == 'M':
            sum = sum - 100
        elif list_Roman[i] == 'C':
            sum += 100
        elif list_Roman[i] == 'V':
            sum += 5
        elif list_Roman[i] == 'L':
            sum += 50
        elif list_Roman[i] == 'D':
            sum += 500
        elif list_Roman[i] == 'M':
            sum += 1000
        else:
            return -1
    return sum
        
        
        
        
# @lc code=end



#
# @lcpr case=start
# "III"\n
# @lcpr case=end

# @lcpr case=start
# "IV"\n
# @lcpr case=end

# @lcpr case=start
# "IX"\n
# @lcpr case=end

# @lcpr case=start
# "LVIII"\n
# @lcpr case=end

# @lcpr case=start
# "MCMXCIV"\n
# @lcpr case=end

#

