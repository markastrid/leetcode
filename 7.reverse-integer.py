#
# @lc app=leetcode.cn id=7 lang=python3
# @lcpr version=30117
#
# [7] 整数反转
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = int(x)
        # 将整数转换为字符串，并反转字符串
        if(x>0):
            reversed_str = str(num)[::-1]
        # 将反转后的字符串转换回整数
            reversed_num = int(reversed_str)
            if(reversed_num>2**31-1):
                return 0
            return reversed_num
        # 输出反转后的整数
        elif (x==0):
            return 0
        else:
            reversed_str=str(num)[:0:-1]
            reversed_num=-int(reversed_str)
            if(reversed_num<-2**31):
                return 0
            return reversed_num
# @lc code=end



#
# @lcpr case=start
# 123\n
# @lcpr case=end

# @lcpr case=start
# -123\n
# @lcpr case=end

# @lcpr case=start
# 120\n
# @lcpr case=end

# @lcpr case=start
# 0\n
# @lcpr case=end

#

