#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#
# https://leetcode.cn/problems/find-the-town-judge/description/
#
# algorithms
# Easy (52.32%)
# Likes:    349
# Dislikes: 0
# Total Accepted:    107.7K
# Total Submissions: 207.3K
# Testcase Example:  '2\n[[1,2]]'
#
# 小镇里有 n 个人，按从 1 到 n 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。
#
# 如果小镇法官真的存在，那么：
#
#
# 小镇法官不会信任任何人。
# 每个人（除了小镇法官）都信任这位小镇法官。
# 只有一个人同时满足属性 1 和属性 2 。
#
#
# 给你一个数组 trust ，其中 trust[i] = [ai, bi] 表示编号为 ai 的人信任编号为 bi 的人。
#
# 如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 -1 。
#
#
#
# 示例 1：
#
#
# 输入：n = 2, trust = [[1,2]]
# 输出：2
#
#
# 示例 2：
#
#
# 输入：n = 3, trust = [[1,3],[2,3]]
# 输出：3
#
#
# 示例 3：
#
#
# 输入：n = 3, trust = [[1,3],[2,3],[3,1]]
# 输出：-1
#
#
#
# 提示：
#
#
# 1 <= n <= 1000
# 0 <= trust.length <= 10^4
# trust[i].length == 2
# trust 中的所有trust[i] = [ai, bi] 互不相同
# ai != bi
# 1 <= ai, bi <= n
#
#
#

# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Counter给出列表值以及对应的数目
        inDegrees = Counter(y for _, y in trust)
        outDegrees = Counter(x for x, _ in trust)
        # next函数用于从生成器中获取下一个元素。如果生成器中存在满足条件的元素，它将返回第一个满足条件的元素。
        # -1：这是next函数的第二个参数，它是一个默认值，用于在生成器中没有找到任何元素时返回。如果生成器中没有找到满足条件的元素，next函数将返回-1
        # return next((i for i in range(1, n + 1) if inDegrees[i] == n - 1 and outDegrees[i] == 0), -1)
        for i in range(1, n+1):
            if inDegrees[i] == n - 1 and outDegrees[i] == 0:
                return i
        return -1
# @lc code=end
