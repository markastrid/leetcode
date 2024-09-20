#
# @lc app=leetcode.cn id=682 lang=python3
# @lcpr version=30121
#
# [682] 棒球比赛
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
      list2=[]
      for i in operations:
        if i=='C':
          list2.pop()
        elif i=="D":
          list2.append(2*list2[-1])
        elif i=="+":
          list2.append(list2[-1]+list2[-2])
        else:
          list2.append(int(i))
      return(sum(list2))
# @lc code=end



#
# @lcpr case=start
# ["5","2","C","D","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["5","-2","4","C","D","9","+","+"]\n
# @lcpr case=end

# @lcpr case=start
# ["1"]\n
# @lcpr case=end

#

