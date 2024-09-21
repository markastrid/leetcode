#
# @lc app=leetcode.cn id=2374 lang=python3
#
# [2374] 边积分最高的节点
#
# https://leetcode.cn/problems/node-with-highest-edge-score/description/
#
# algorithms
# Medium (41.96%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    18.7K
# Total Submissions: 38.8K
# Testcase Example:  '[1,0,0,0,0,7,7,5]'
#
# 给你一个有向图，图中有 n 个节点，节点编号从 0 到 n - 1 ，其中每个节点都 恰有一条 出边。
#
# 图由一个下标从 0 开始、长度为 n 的整数数组 edges 表示，其中 edges[i] 表示存在一条从节点 i 到节点 edges[i] 的 有向
# 边。
#
# 节点 i 的 边积分 定义为：所有存在一条指向节点 i 的边的节点的 编号 总和。
#
# 返回 边积分 最高的节点。如果多个节点的 边积分 相同，返回编号 最小 的那个。
#
#
#
# 示例 1：
#
# 输入：edges = [1,0,0,0,0,7,7,5]
# 输出：7
# 解释：
# - 节点 1、2、3 和 4 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 + 3 + 4 = 10 。
# - 节点 0 有一条指向节点 1 的边，节点 1 的边积分等于 0 。
# - 节点 7 有一条指向节点 5 的边，节点 5 的边积分等于 7 。
# - 节点 5 和 6 都有指向节点 7 的边，节点 7 的边积分等于 5 + 6 = 11 。
# 节点 7 的边积分最高，所以返回 7 。
#
#
# 示例 2：
#
# 输入：edges = [2,0,0,2]
# 输出：0
# 解释：
# - 节点 1 和 2 都有指向节点 0 的边，节点 0 的边积分等于 1 + 2 = 3 。
# - 节点 0 和 3 都有指向节点 2 的边，节点 2 的边积分等于 0 + 3 = 3 。
# 节点 0 和 2 的边积分都是 3 。由于节点 0 的编号更小，返回 0 。
#
#
#
#
# 提示：
#
#
# n == edges.length
# 2 <= n <= 10^5
# 0 <= edges[i] < n
# edges[i] != i
#
#
#

# @lc code=start
class Solution:
    def edgeScore(self, edges: List[int]) -> int:
        '''
        n = len(edges)
        # 下面找到所有有非零边积分的点，即数组中不重复子数
        New_Edge = list(set(edges))
        # 对New_Edge中每个元素到其对应的边积分创造一个字典，这样在下面的计算中能够直接算出字典序
        dict_edge = {}
        for i in New_Edge:
            dict_edge[i] = 0
        # 这样完成对里面的计算
        for i in range(n):
            for j in range(len(New_Edge)):
                if edges[i] == New_Edge[j]:
                    dict_edge[New_Edge[j]] = dict_edge[New_Edge[j]]+i
        # 计算每个边积分已经解决
        # print(dict_edge)
        # 下一步:对其排序，并在相同时返回小的那个，那么需要稳定排序
        # 这里排序的结果是一个元组
        sorted_items = sorted(
            dict_edge.items(), key=lambda item: item[1], reverse=True)
        # print(sorted_items[0][0])
        return sorted_items[0][0]
        '''
        # 上述方法是可行的，但是会超限
        # 查阅得到可以有线性时间的解决
        # 用enumerate()同时获得下标和值，一次遍历解决
        # 记录所有点的得分
        score = [0] * len(edges)
        # 记录最大边积分和对应的下标，这是为了保证相同的时候取最小的下标
        max_num = 0
        max_num_index = len(edges)
        for index, num in enumerate(edges):
            score[num] += index
            if score[num] > max_num or (score[num] == max_num and max_num_index > num):
                max_num = score[num]
                max_num_index = num
        return max_num_index
# @lc code=end
