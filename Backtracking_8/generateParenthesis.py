'''
22. 括号生成
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
示例：
输入：n = 3
输出：[
       "((()))",
       "(()())",
       "(())()",
       "()(())",
       "()()()"
     ]
'''
class Solution(object):
    def generateParenthesis(self, n):
        if n==0:return []
        res = []
        current = ''
        self.dfs(res,current,n,n)
        return res
    def dfs(self,res,current,left,right):
        if left==0 and right==0:
            res.append(current)
            return
        if left<0 or left>right:
            return
        self.dfs(res,current+'(',left-1,right)
        self.dfs(res,current+')',left,right-1)