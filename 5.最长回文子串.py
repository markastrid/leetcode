#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (37.36%)
# Likes:    7410
# Dislikes: 0
# Total Accepted:    1.8M
# Total Submissions: 4.7M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的 回文 子串。
#
#
#
# 示例 1：
#
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#
#
# 示例 2：
#
#
# 输入：s = "cbbd"
# 输出："bb"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 仅由数字和英文字母组成
#
#
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # DP[i]表示i下标为中心的回文序列
        max_len = 1
        index = 0
        length = len(s)
        DP = [[False for _ in range(length)] for _ in range(length)]
        for j in range(1, length):
            for i in range(j):
                # 必须 j 在外层、i 在内层，才能确保遍历到当前子串的时候，当前子串的子串已经全部遍历过
                if j-i < 3:
                    if s[i] == s[j]:
                        DP[i][j] = True
                else:
                    if DP[i+1][j-1] and s[i] == s[j]:
                        DP[i][j] = True
                if j-i+1 > max_len and DP[i][j]:
                    max_len = j-i+1
                    index = i
        return s[index:index+max_len]

        # @lc code=end
