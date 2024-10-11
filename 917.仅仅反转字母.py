#
# @lc app=leetcode.cn id=917 lang=python3
#
# [917] 仅仅反转字母
#
# https://leetcode.cn/problems/reverse-only-letters/description/
#
# algorithms
# Easy (59.67%)
# Likes:    215
# Dislikes: 0
# Total Accepted:    86.2K
# Total Submissions: 145.2K
# Testcase Example:  '"ab-cd"'
#
# 给你一个字符串 s ，根据下述规则反转字符串：
#
#
# 所有非英文字母保留在原有位置。
# 所有英文字母（小写或大写）位置反转。
#
#
# 返回反转后的 s 。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：s = "ab-cd"
# 输出："dc-ba"
#
#
#
#
#
# 示例 2：
#
#
# 输入：s = "a-bC-dEf-ghIj"
# 输出："j-Ih-gfE-dCba"
#
#
#
#
#
# 示例 3：
#
#
# 输入：s = "Test1ng-Leet=code-Q!"
# 输出："Qedo1ct-eeLg=ntse-T!"
#
#
#
#
# 提示
#
#
# 1 <= s.length <= 100
# s 仅由 ASCII 值在范围 [33, 122] 的字符组成
# s 不含 '\"' 或 '\\'
#
#
#

# @lc code=start
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        '''
        # 完全反转的结果
        res = s
        # 大写字母A-Z的ASCII码为:65-90;小写字母a-z的ASCII码为:97-122
        # 创造一个字典记录所有非英文字母的位置
        dict = {}
        for i in range(len(s)):
            if ord(s[i]) < 65 or 90 < ord(s[i]) < 97:
                dict[s[i]] = i
        for i in range(len(res)):
            if ord(res[i]) < 65 or 90 < ord(res[i]) < 97:
                res = res.replace(res[i], "")
            if len(res)-1 < i:
                break
        print(res)
        '''
        # 双指针解决
        left = 0
        right = len(s)-1
        ans = list(s)
        while left < right:
            while not ans[left].isalpha():
                if left >= right:
                    break
                left += 1
            while not ans[right].isalpha():
                if left >= right:
                    break
                right -= 1
            if left >= right:
                break
            ans[left], ans[right] = ans[right], ans[left]
            left += 1
            right -= 1
        return ''.join(ans)

# @lc code=end
