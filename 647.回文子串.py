#
# @lc app=leetcode.cn id=647 lang=python3
#
# [647] 回文子串
#
# https://leetcode.cn/problems/palindromic-substrings/description/
#
# algorithms
# Medium (66.91%)
# Likes:    1380
# Dislikes: 0
# Total Accepted:    362.3K
# Total Submissions: 535.6K
# Testcase Example:  '"abc"'
#
# 给你一个字符串 s ，请你统计并返回这个字符串中 回文子串 的数目。
#
# 回文字符串 是正着读和倒过来读一样的字符串。
#
# 子字符串 是字符串中的由连续字符组成的一个序列。
#
#
#
# 示例 1：
#
#
# 输入：s = "abc"
# 输出：3
# 解释：三个回文子串: "a", "b", "c"
#
#
# 示例 2：
#
#
# 输入：s = "aaa"
# 输出：6
# 解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# s 由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str) -> int:
        DP = [[False for _ in range(len(s))] for _ in range(len(s))]
        max_count = 0
        for i in range(len(s)):
            DP[i][i] == True
        max_count += len(s)
        for j in range(1, len(s)):
            for i in range(j):
                if j-i < 3 and s[i] == s[j]:
                    DP[i][j] = True
                    max_count += 1
                else:
                    if DP[i+1][j-1] and s[i] == s[j]:
                        DP[i][j] = True
                        max_count += 1

        return max_count

# @lc code=end
