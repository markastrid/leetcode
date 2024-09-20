#
# @lc app=leetcode.cn id=2376 lang=python3
#
# [2376] 统计特殊整数
#
# https://leetcode.cn/problems/count-special-integers/description/
#
# algorithms
# Hard (49.68%)
# Likes:    114
# Dislikes: 0
# Total Accepted:    17.6K
# Total Submissions: 30.2K
# Testcase Example:  '20'
#
# 如果一个正整数每一个数位都是 互不相同 的，我们称它是 特殊整数 。
# 
# 给你一个 正 整数 n ，请你返回区间 [1, n] 之间特殊整数的数目。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 20
# 输出：19
# 解释：1 到 20 之间所有整数除了 11 以外都是特殊整数。所以总共有 19 个特殊整数。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 5
# 输出：5
# 解释：1 到 5 所有整数都是特殊整数。
# 
# 
# 示例 3：
# 
# 
# 输入：n = 135
# 输出：110
# 解释：从 1 到 135 总共有 110 个整数是特殊整数。
# 不特殊的部分数字为：22 ，114 和 131 。
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 2 * 10^9
# 
# 
#

# @lc code=start
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
      '''
      #我们需要制造一个可以判断单个整数是否每个位置都互不相同的函数，然后从1-n循环调用这个函数
      #特殊整数的数量
      Special_Count=0
      def is_special_count(number):
        #转化为str类型
        Special_Str=str(number)
        #用一个数组进行对应个数的储存，如果有就+1，没有就是0，大于1则不是互不相同
        Special_Array=[0,0,0,0,0,0,0,0,0,0]
        #对每个数组进行遍历
        for i in range(len(Special_Str)):
          Special_Array[int(Special_Str[i])]=Special_Array[int(Special_Str[i])]+1
        flag=True
        #print(len(Special_Array))
        #print(Special_Array)
        for i in range(len(Special_Array)):
          #print(Special_Array[i])
          if Special_Array[i]>1:
            flag=False
        return flag
      for i in range(1,n+1):
        if is_special_count(i):
          Special_Count=Special_Count+1
      return Special_Count
      '''
      #上述方法可行，但是时间会超出，因此需要考虑优化方法
      #一个个找显然是太麻烦的，根据官方解析的思想，我们可以把它分成两部分:一部分是小于k位数的数字，这里做组合数学就能够直接算出；对于大于k位的数字我们进行相应的计算，这个后面再说
      #优化的方法如下
      #1.对于小于k位的数字(十进制下的k个位数)，采取组合数学的方法进行计算，最高位可选9个(1-9)，其次也是9个(0-9-最高位选过的)，后面依次递减即可计算出总的数字
      #2.对于等于k位的数字，这里确实暂时不会计算
      
# @lc code=end

