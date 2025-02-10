#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode.cn/problems/minimum-window-substring/description/
#
# algorithms
# Hard (45.07%)
# Likes:    3053
# Dislikes: 0
# Total Accepted:    672K
# Total Submissions: 1.4M
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 ""
# 。
#
#
#
# 注意：
#
#
# 对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
# 如果 s 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
#
# 示例 1：
#
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。
#
#
# 示例 2：
#
#
# 输入：s = "a", t = "a"
# 输出："a"
# 解释：整个字符串 s 是最小覆盖子串。
#
#
# 示例 3:
#
#
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。
#
#
#
# 提示：
#
#
# ^m == s.length
# ^n == t.length
# 1 <= m, n <= 10^5
# s 和 t 由英文字母组成
#
#
#
# 进阶：你能设计一个在 o(m+n) 时间内解决此问题的算法吗？
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans_left = -1
        # 必须要够大，因为这样才能成功进行左边的删减
        # 比如说，第一次right就到了最右边，这时候如果这里的ans_right不够大，就无法在这个left->right之间进行删减获得一个答案
        ans_right = len(s)-1
        s_count = Counter()
        t_count = Counter(t)
        left = 0
        # 同时获得数组和值
        for right, num in enumerate(s):
            s_count[num] += 1
            while s_count >= t_count:
                if right-left < ans_right-ans_left:
                    ans_left, ans_right = left, right
                s_count[s[left]] -= 1
                left += 1
        return "" if ans_left == -1 else s[ans_left:ans_right+1]
        # 优化：less维护-灵茶山艾府-后续跟进

# @lc code=end
