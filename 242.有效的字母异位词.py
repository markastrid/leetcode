#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode.cn/problems/valid-anagram/description/
#
# algorithms
# Easy (65.77%)
# Likes:    949
# Dislikes: 0
# Total Accepted:    843.8K
# Total Submissions: 1.3M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的 字母异位词。
#
#
#
# 示例 1:
#
#
# 输入: s = "anagram", t = "nagaram"
# 输出: true
#
#
# 示例 2:
#
#
# 输入: s = "rat", t = "car"
# 输出: false
#
#
#
# 提示:
#
#
# 1 <= s.length, t.length <= 5 * 10^4
# s 和 t 仅包含小写字母
#
#
#
#
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
#
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 判断是否是字母异位词
        # 我的第一个想法是把它们按照unicode字符集中的数字大小进行排列，这样依次比较，异位词的每个位数就是完全相同的
        # 首先长度不一样直接排除
        if len(s) != len(t):
            return False
        '''
        # 用ord()函数进行转化成unicode这样可比大小
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                print(s[i])
                if ord(s[i]) < ord(s[j]):
                    s[i], s[j] = s[j], s[i]
                    t[i], t[j] = t[j], t[i]
        # 理论上来说，这里已经完成了交换，这样如果是字母异位词就完全相同了
        '''
        s = sorted(s)
        t = sorted(t)
        for i in range(len(s)):
            if s[i] != t[i]:
                return False
        return True
        # @lc code=end
