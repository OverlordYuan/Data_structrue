'''
322. 零钱兑换
给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。
示例 1:
输入: coins = [1, 2, 5], amount = 11
输出: 3
解释: 11 = 5 + 5 + 1
示例 2:
输入: coins = [2], amount = 3
输出: -1
 说明:
你可以认为每种硬币的数量是无限的。
'''
class Solution(object):
    def coinChange(self, coins, amount):
        if amount==0 or len(coins)==0:return 0
        dp = [amount+1 for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                if j>=coins[i]:
                    dp[j] = min(dp[j-coins[i]]+1,dp[j])
        if dp[-1] == amount+1:return -1
        else:return dp[-1]
if __name__ == '__main__':
    a = Solution()
    s = [2]
    c = 3
    res = a.coinChange(s,c)
    print(res)