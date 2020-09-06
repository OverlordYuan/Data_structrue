'''
64. 最小路径和
给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。
说明：每次只能向下或者向右移动一步。
示例:
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
'''
class Solution(object):
    def minPathSum(self, grid):
        if len(grid)==0:return 0
        if len(grid)==1:return sum(grid[0])
        m = len(grid)
        n = len(grid[0])
        dp = [grid[0][0]]

        for k in range(1,n):
            dp.append(grid[0][k]+dp[-1])
        for i in range(1,m):
            for j in range(n):
                if j==0:
                    dp[j] = dp[j] + grid[i][j]
                else:
                    dp[j] = min(dp[j],dp[j-1])+ grid[i][j]
        return dp[-1]
if __name__ == '__main__':
    s = [
        [1,3,1],
        [1,5,1],
        [4,2,1]
    ]
    a = Solution()
    RES = a.minPathSum(s)
    print(RES)