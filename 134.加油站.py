#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
# https://leetcode.cn/problems/gas-station/description/
#
# algorithms
# Medium (52.39%)
# Likes:    1726
# Dislikes: 0
# Total Accepted:    427K
# Total Submissions: 898.7K
# Testcase Example:  '[1,2,3,4,5]\n[3,4,5,1,2]'
#
# 在一条环路上有 n 个加油站，其中第 i 个加油站有汽油 gas[i] 升。
#
# 你有一辆油箱容量无限的的汽车，从第 i 个加油站开往第 i+1 个加油站需要消耗汽油 cost[i] 升。你从其中的一个加油站出发，开始时油箱为空。
#
# 给定两个整数数组 gas 和 cost ，如果你可以按顺序绕环路行驶一周，则返回出发时加油站的编号，否则返回 -1 。如果存在解，则 保证 它是 唯一
# 的。
#
#
#
# 示例 1:
#
#
# 输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
# 输出: 3
# 解释:
# 从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
# 开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
# 开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
# 开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
# 开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
# 开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
# 因此，3 可为起始索引。
#
# 示例 2:
#
#
# 输入: gas = [2,3,4], cost = [3,4,3]
# 输出: -1
# 解释:
# 你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
# 我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
# 开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
# 开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
# 你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
# 因此，无论怎样，你都不可能绕环路行驶一周。
#
#
#
# 提示:
#
#
# gas.length == n
# cost.length == n
# 1 <= n <= 10^5
# 0 <= gas[i], cost[i] <= 10^4
#
#
#

# @lc code=start
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 因为存在唯一解，因此我们从油最多的一个站开始即可，不存在都可以的情况
        # 上面的想法有点错误，不是油最多的一个站，而是到下一个站剩下最多油的一个站，这样能够对于下一个站来说是当前的开始的最好选择
        '''
        remain_gas = [gas[i]-cost[i] for i in range(len(gas))]
        max_gas = max(remain_gas)
        max_index = remain_gas.index(max_gas)
        # 这里的max_index是到下一个站所需要最少的距离，从这里开始
        new_gas = gas[max_index:len(gas)]+gas[0:max_index]
        new_cost = cost[max_index:len(cost)]+cost[0:max_index]
        new_remain_gas = remain_gas[max_index:len(
            remain_gas)]+remain_gas[0:max_index]
        gas_remain = 0
        for i in range(len(gas)):
            gas_remain += new_remain_gas[i]
            if gas_remain < 0:
                return -1
        return max_index
        '''
      # 果然上面的方法没有全过，这里考虑到这样一点:有多个最大值的时候选择哪个的问题，感觉我的贪心并不能解决所有问题，如对于这个例子就不行
      # [5,8,2,8]
      # [6,5,6,6]
      # 所以应该是跟之前一样，分两步，一步是当前的最大，一步是当前最大限度内到下一步的最大，类似45\55
      # 再次更新，采用枚举+贪心的方法
      # 从当前节点出来，如果能走n步直接回来，那么就成功了
      # 如果不能走n步，假设只能走k步，那么下一步就从当前节点+k+1开始尝试
      # 因为如果当前节点走不了，当前节点到k之间的节点一定走不了
        n = len(gas)
        remain = [gas[i]-cost[i] for i in range(len(gas))]
        i = 0
        # 这里用while是因为下面i有自+操作
        while i < n:
            remain_gas = 0
            step = 0
            while step < n:
                count = (i+step) % n
                remain_gas += remain[count]
                if remain_gas < 0:
                    break
                step += 1
            if step == n:
                return i
            i += step+1
        return -1


# @lc code=end
