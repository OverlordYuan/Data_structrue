'''
221. 最大正方形
在一个由 0 和 1 组成的二维矩阵内，找到只包含 1 的最大正方形，并返回其面积。
示例:
输入:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
输出: 4
'''
class Solution(object):
    def maximalSquare(self, matrix):
        m = len(matrix)
        if m == 0:return 0
        n = len(matrix[0])
        res = 0
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    dp[i+1][j+1] = min(dp[i][j],dp[i+1][j],dp[i][j+1])+1
                    res = max(res,dp[i+1][j+1])
        return res