'''
96. 不同的二叉搜索树
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''
class Solution(object):
    def numTrees(self, n):
        if n<1:return 1
        dp = []
        for i in range(n+1):
            if i<2:
                dp.append(1)
            else:
                temp = 0
                for j in range(i):
                    temp += dp[j]*dp[i-j-1]
                dp.append(temp)
        return dp[-1]

if __name__ == '__main__':

    a  = Solution()
    s = 3
    res = a.numTrees(s)
    print(res)