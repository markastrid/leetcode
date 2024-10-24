#
# @lc app=leetcode.cn id=118 lang=python3
#
# [118] 杨辉三角
#
# https://leetcode.cn/problems/pascals-triangle/description/
#
# algorithms
# Easy (75.57%)
# Likes:    1189
# Dislikes: 0
# Total Accepted:    572.8K
# Total Submissions: 747.6K
# Testcase Example:  '5'
#
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
#
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。
#
#
#
#
#
# 示例 1:
#
#
# 输入: numRows = 5
# 输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
#
# 示例 2:
#
#
# 输入: numRows = 1
# 输出: [[1]]
#
#
#
#
# 提示:
#
#
# 1
#
#
#

# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
        #正常的思路
        ans = []
        for i in range(numRows):
            j = 1
            single_nas = [1]
            while j < i :
                single_nas.append(ans[i-1][j-1]+ans[i-1][j])
                j += 1
            if i > 0:
                single_nas.append(1)
            ans.append(single_nas)
        return ans
        '''
        # 从力扣那里找到的一些思路：当前一行只比上一行多了一个元素本行元素等于上一行元素往后错一位再逐个相加
        # 因此找当前行元素时对之前的最后一行相加减即可
        # zip接受一系列可迭代的对象作为参数，将对象中对应的元素打包成一个个tuple（元组），然后返回由这些tuples组成的list（列表）
        if numRows == 0:
            return []
        ans = [[1]]
        i = 1
        while i < numRows:
            ans.append([a+b for (a, b) in zip([0]+ans[-1], ans[-1]+[0])])
            i += 1
        return ans

# @lc code=end
