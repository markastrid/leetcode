#
# @lc app=leetcode.cn id=225 lang=python3
# @lcpr version=30121
#
# [225] 用队列实现栈
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class MyStack:

    def __init__(self):
      self.queue1=[]

    def push(self, x: int) -> None:
      self.queue1.append(x)

    def pop(self) -> int:
      return self.queue1.pop()

    def top(self) -> int:
      return self.queue1[-1]

    def empty(self) -> bool:
      if (len(self.queue1)==0):
        return True
      return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end



#
# @lcpr case=start
# ["MyStack", "push", "push", "top", "pop", "empty"][[], [1], [2], [], [], []]\n
# @lcpr case=end

#

