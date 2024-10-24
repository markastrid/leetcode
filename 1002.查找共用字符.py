#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#
# https://leetcode.cn/problems/find-common-characters/description/
#
# algorithms
# Easy (71.29%)
# Likes:    377
# Dislikes: 0
# Total Accepted:    99.1K
# Total Submissions: 140.9K
# Testcase Example:  '["bella","label","roller"]'
#
# 给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（包括重复字符），并以数组形式返回。你可以按 任意顺序
# 返回答案。
#
#
# 示例 1：
#
#
# 输入：words = ["bella","label","roller"]
# 输出：["e","l","l"]
#
#
# 示例 2：
#
#
# 输入：words = ["cool","lock","cook"]
# 输出：["c","o"]
#
#
#
#
# 提示：
#
#
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] 由小写英文字母组成
#
#
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = [float("inf")]*26
        for i in words:
            freq = [0]*26
            for j in range(len(i)):
                freq[ord(i[j])-ord('a')] += 1
            for k in range(26):
                min_freq[k] = min(min_freq[k], freq[k])
        ans = []
        #print(min_freq)
        for i in range(26):
            while min_freq[i] > 0:
                ans.append(chr(i+ord('a')))
                min_freq[i] -= 1
        return ans

        # @lc code=end
