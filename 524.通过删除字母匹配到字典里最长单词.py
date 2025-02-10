#
# @lc app=leetcode.cn id=524 lang=python3
#
# [524] 通过删除字母匹配到字典里最长单词
#
# https://leetcode.cn/problems/longest-word-in-dictionary-through-deleting/description/
#
# algorithms
# Medium (50.03%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    112.4K
# Total Submissions: 223.1K
# Testcase Example:  '"abpcplea"\n["ale","apple","monkey","plea"]'
#
# 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s
# 中的某些字符得到。
#
# 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
#
#
#
# 示例 1：
#
#
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
#
#
# 示例 2：
#
#
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
#
#
#
#
# 提示：
#
#
# 1 <= s.length <= 1000
# 1 <= dictionary.length <= 1000
# 1 <= dictionary[i].length <= 1000
# s 和 dictionary[i] 仅由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        # 先按照字母序排好
        dictionary = sorted(dictionary)
        # 依次遍历
        ans_len = 0
        ans = ""
        for i in dictionary:
            # left、right用来遍历s
            # ans_left、ans_right用来遍历当前的i
            left = 0
            right = len(s)-1
            ans_left = 0
            ans_right = len(i)-1
            while left <= right:
                if i[ans_left] == s[left]:
                    ans_left += 1
                if i[ans_right] == s[right]:
                    ans_right -= 1
                # 记录符合的数组，而且总是记录最长的且字母顺序最小的那个
                # 字母顺序由前面的sort保证:长度相同取前面的那个
                # 长度由下面的比较保证
                if ans_left > ans_right:
                    if ans_len < len(i):
                        ans_len = len(i)
                        ans = i
                    # 达到这次while的中止了：s或者当前的字符串遍历完，前者由while循环保证，后者由这个判断保证，同时判断需要承担记录当前记录最长字符串的功能
                    break
                left += 1
                right -= 1
        return ans


# @lc code=end
