#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] 去除重复字母
#
# https://leetcode.cn/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (48.23%)
# Likes:    1109
# Dislikes: 0
# Total Accepted:    147.6K
# Total Submissions: 299.1K
# Testcase Example:  '"bcabc"'
#
# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。
#
#
#
# 示例 1：
#
#
# 输入：s = "bcabc"
# 输出："abc"
#
#
# 示例 2：
#
#
# 输入：s = "cbacdcbc"
# 输出："acdb"
#
#
#
# 提示：
#
#
# 1 <= s.length <= 10^4
# s 由小写英文字母组成
#
#
#
#
# 注意：该题与 1081
# https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters
# 相同
#
#

# @lc code=start
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 去除重复字母后的字典序号最小：字典序遵循的是逐字符比较的方式,越靠左的字符越会被先比较
        # 官解贪心的思路：给定一个字符串 s，如何去掉其中的一个字符 ch，使得得到的字符串字典序最小呢？答案是：在重复中找出最小的满足 s[i]>s[i+1] 的下标 i，并去除字符 s[i]。
        # 评论优化： 一个字符串的字典序, 取决于下标更小的字符的大小, 从左往右遍历的过程中, 如果发现当前字符(下标为i)的大小比前一个字符(下标为i-1)小的话, 就可以考虑删除前一个字符(下表为i-1),当前是在其重复的情况下，让当前字符到下标更小的地方, 使得最终的字典序更小
        # 不重复列表
        list_s = list(set(s))
        answer = []
        dict = {}
        set_ans = set()
        for i in range(len(list_s)):
            dict[list_s[i]] = 0
        for i in range(len(s)):
            dict[s[i]] += 1
        for i in range(len(s)):
            if s[i] in set_ans:
                dict[s[i]] -= 1
                continue
            if dict[s[i]] == 0:
                continue
            # 要用while，因为去除前一个之后，可能前一个的前一个也会小哦
            while answer and s[i] < answer[-1] and dict[answer[-1]] > 0:
                set_ans.remove(answer.pop())
            answer.append(s[i])
            dict[s[i]] -= 1
            set_ans.add(s[i])

        return ''.join(answer)
        # @lc code=end
