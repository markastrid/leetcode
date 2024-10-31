#
# @lc app=leetcode.cn id=1025 lang=python3
#
# [1025] 除数博弈
#
# https://leetcode.cn/problems/divisor-game/description/
#
# algorithms
# Easy (70.67%)
# Likes:    432
# Dislikes: 0
# Total Accepted:    107.6K
# Total Submissions: 151.9K
# Testcase Example:  '2'
#
# 爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。
#
# 最初，黑板上有一个数字 n 。在每个玩家的回合，玩家需要执行以下操作：
#
#
# 选出任一 x，满足 0 < x < n 且 n % x == 0 。
# 用 n - x 替换黑板上的数字 n 。
#
#
# 如果玩家无法执行这些操作，就会输掉游戏。
#
# 只有在爱丽丝在游戏中取得胜利时才返回 true 。假设两个玩家都以最佳状态参与游戏。
#
#
#
#
#
#
# 示例 1：
#
#
# 输入：n = 2
# 输出：true
# 解释：爱丽丝选择 1，鲍勃无法进行操作。
#
#
# 示例 2：
#
#
# 输入：n = 3
# 输出：false
# 解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。
#
#
#
#
# 提示：
#
#
# 1 <= n <= 1000
#
#
#

# @lc code=start
class Solution:
    def divisorGame(self, n: int) -> bool:
        '''
        通俗一点的解释

        因为至少可以取1 ,所以最后决胜负的时候 就是谁取到1 就输了

        拿到奇数时 : 只有一种选择 就是 减去 奇数 , 给出偶数

        拿到偶数的时候: 有 2 种选择 1. 减去奇数返回奇数; 2.减去偶数 返回偶数

        可见 拿到偶数的人 有能力选择保持另一个人 奇偶性 永远是 奇数

        由于拿到1的人就输 所以 偶数能一直保持 另一个人是奇数 , 且值一定不停的在减少趋向于 1 所以 开始手里是偶数的人能赢
        '''

        return n % 2 == 0
        '''
        # DP法
        DP = [False for i in range(n+5)]
        DP[1] = False
        DP[2] = True
        for i in range(3, n+1):
            for j in range(1, i):
                if i % j == 0 and DP[i-j] == False:
                    DP[i] = True
                    break
        return DP[n]
        '''
# @lc code=end
