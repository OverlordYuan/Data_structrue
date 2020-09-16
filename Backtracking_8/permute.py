'''
46. 全排列
给定一个 没有重复 数字的序列，返回其所有可能的全排列。
示例:
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
'''
import copy
class Solution(object):
    def permute(self, nums):
        res = []
        used = [False for item in nums]
        self.dfs(res,[],nums,used)
        return res

    def dfs(self,res,current,nums,used):
        if len(current)==len(nums):
            res.append(copy.deepcopy(current))
            return
        for i in range(len(nums)):
            if used[i]==False:
                current.append(nums[i])
                used[i] = True
                self.dfs(res,current,nums,used)
                used[i] = False
                current.pop()
if __name__ == '__main__':
    s = [1,2,3]
    t = 7
    a = Solution()
    RES = a.permute(s)
    print(RES)