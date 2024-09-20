#
# @lc app=leetcode.cn id=496 lang=python3
# @lcpr version=30121
#
# [496] 下一个更大元素 I
#


# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
      '''
      #首先想到最nt的方法:三层循环
      #能通过，但是超越整整5.43%的人，真是太有实力了
      #直接寻求帮忙
      nums=[]
      flag=False
      for i in range(len(nums1)):
        for j in range(len(nums2)):
          if nums1[i]==nums2[j]:
            #注意这里顺序，不能重新从0 开始这个nums2数组
            for k in nums2[j+1::]:
              if k>nums2[j]:
                flag=True
                break
            if flag==True:
              nums.append(k)
              flag=False
            else:
              nums.append(-1)
      return nums
      '''
      
      '''
      遍历nums2，建立一个单调递减栈，遇到比栈顶更大元素i，则从栈顶开始，依次弹出，同步更新弹出元素对应的下一个最大元素，即当前值i，记录到哈希表中;最后，通过查哈希表获取nums1中每个值对应的下一个最大元素，若不在表中则返回-1。
      '''
      stack=[]
      hash={}
      for i in nums2:
        while stack  and stack[-1]<i:
          hash[stack[-1]]=i
          stack.pop()
        stack.append(i)
      return [hash[i] if i in hash else -1 for i in nums1]
# @lc code=end



#这里测试集的形式好像有问题，多了个点,我把删除了以及
# @lcpr case=start
# [4,1,2]\n[1,3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,4]\n[1,2,3,4]\n
# @lcpr case=end

#

