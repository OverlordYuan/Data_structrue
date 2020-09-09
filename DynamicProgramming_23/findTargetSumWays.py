'''
494. 目标和
给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。
返回可以使最终数组和为目标数 S 的所有添加符号的方法数。
示例：
输入：nums: [1, 1, 1, 1, 1], S: 3
输出：5
解释：
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
一共有5种方法让最终目标和为3。
 提示：
数组非空，且长度不会超过 20 。
初始的数组的和不会超过 1000 。
保证返回的最终结果能被 32 位整数存下。
'''
class Solution(object):
    def findTargetSumWays(self, nums, S):
        sums = sum(nums)
        if sums<S or (sums+S)%2!=0:return 0
        target = (sums+S)//2
        dp = [0 for i in range(target+1)]
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j] += dp[j-nums[i]]
        return dp[-1]
if __name__ == '__main__':
    a = Solution()
    S = [1,1,1,1,1]
    T = 3
    res = a.findTargetSumWays(S,T)
    print(res)