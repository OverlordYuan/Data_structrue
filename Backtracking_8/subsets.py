'''
78. 子集
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
说明：解集不能包含重复的子集。
示例:
输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
import copy
class Solution(object):
    def subsets(self, nums):
        res = []
        curent = []
        self.dfs(res,curent,nums)
        return res
    def dfs(self,res,current,nums):
        res.append(copy.deepcopy(current))
        for i in range(len(nums)):
            current.append(nums[i])
            self.dfs(res,current,nums[i+1:])
            current.pop()