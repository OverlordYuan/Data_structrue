'''
152. 乘积最大子数组
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
示例 1:
输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:
输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
'''
class Solution(object):
    def maxProduct(self, nums):
        if len(nums)==1:return nums[0]
        dp0 = nums[0]
        dp1 = nums[0]
        res = nums[0]
        for i in range(1,len(nums)):
            temp0 = max(dp0*nums[i],dp1*nums[i],nums[i])
            temp1 = min(dp0*nums[i],dp1*nums[i],nums[i])
            dp0 = temp0
            dp1 = temp1
            res = max(dp0,res)
        return res
if __name__ == '__main__':
    a = Solution()
    S = [-4,-3,-2]
    RES = a.maxProduct(S)
    print(RES)