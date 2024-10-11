#
# @lc app=leetcode.cn id=1081 lang=python3
#
# [1081] 不同字符的最小子序列
#
# https://leetcode.cn/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (58.29%)
# Likes:    216
# Dislikes: 0
# Total Accepted:    31.8K
# Total Submissions: 53.4K
# Testcase Example:  '"bcabc"'
#
# 返回 s 字典序最小的子序列，该子序列包含 s 的所有不同字符，且只包含一次。
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
# 1 <= s.length <= 1000
# s 由小写英文字母组成
#
#
#
#
# 注意：该题与 316 https://leetcode.cn/problems/remove-duplicate-letters/ 相同
#
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # 这里是对316题的相应学习和重构
        # 理清思路：我们返回字典序最小的子序列，需要依次遍历序列，之后如果当前的字母比前一个字母小，那么就删除前一个字母（在重复的情况下，这里的删除是循环的，即删完前一个再判断前一个的前一个，直到不满足循环要求）；
        # 先用列表，结束的时候再转换成字符串即可，较为方便
        ans = []
        # set集合用来存储不重复的字母集,和之前用的字典统计相同
        count = Counter(s)
        ans_set = set()
        for i in s:
            count[i] -= 1
            if i in ans_set:
                continue
            while ans and i < ans[-1] and count[ans[-1]]:
                ans_set.remove(ans.pop())
            ans_set.add(i)
            ans.append(i)
        return "".join(ans)
        '''
        #下面这个是限制改为limit个数的情况，注意有一些小小的区分
        class Solution(object):
    def arrangeBookshelf(self, order, limit):
        """
        :type order: List[int]
        :type limit: int
        :rtype: List[int]
        """
        ans = []
        # set集合用来存储不重复的字母集,和之前用的字典统计相同
        count = Counter(order)
        ans_set = Counter()
        for i in order:
            count[i] -= 1
            if ans_set[i]==limit:
                continue
            #这里与之前两道题的不同在于，保留多个的时候注意优先级和顺序:ans_set[ans[-1]]是最后一个在队列中的，count[ans[-1]]则是剩下的，如果和小于等于limit就不能操作了，因为这样就会多拿书
            while ans and i < ans[-1] and ans_set[ans[-1]]+count[ans[-1]]>limit:
                ans_set[ans.pop()]-=1
            ans_set[i]+=1
            ans.append(i)
        return ans
        
        '''
        # @lc code=end
