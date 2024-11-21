#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#
# https://leetcode.cn/problems/partition-labels/description/
#
# algorithms
# Medium (76.88%)
# Likes:    1210
# Dislikes: 0
# Total Accepted:    285.3K
# Total Submissions: 367.4K
# Testcase Example:  '"ababcbacadefegdehijhklij"'
#
# 给你一个字符串 s 。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。
#
# 注意，划分结果需要满足：将所有划分结果按顺序连接，得到的字符串仍然是 s 。
#
# 返回一个表示每个字符串片段的长度的列表。
#
#
# 示例 1：
#
#
# 输入：s = "ababcbacadefegdehijhklij"
# 输出：[9,7,8]
# 解释：
# 划分结果为 "ababcbaca"、"defegde"、"hijhklij" 。
# 每个字母最多出现在一个片段中。
# 像 "ababcbacadefegde", "hijhklij" 这样的划分是错误的，因为划分的片段数较少。
#
# 示例 2：
#
#
# 输入：s = "eccbbbbdec"
# 输出：[10]
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 500
# s 仅由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dict_s = {}
        # 所有字母对应的最后的尾标
        for i in range(len(s)):
            if s[i] not in dict_s:
                dict_s[s[i]] = i
            else:
                dict_s[s[i]] = i
        ans = []
        start = 0
        end = 0
        for i in range(len(s)):
            end = max(end, dict_s[s[i]])
            if i == end:
                ans.append(end-start+1)
                start = end+1
        return ans

# @lc code=end
