'''
79. 单词搜索
给定一个二维网格和一个单词，找出该单词是否存在于网格中。
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
示例:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
提示：
board 和 word 中只包含大写和小写英文字母。
1 <= board.length <= 200
1 <= board[i].length <= 200
1 <= word.length <= 10^3
'''
class Solution(object):
    def __init__(self):
        self.flag = False
    def exist(self, board, word):
        if board == [] or len(board[0])==0:return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if self.dfs(board,i,j,word,0):
                    return True
        return False
    def dfs(self,board,m,n,word,cur):
        if cur==len(word):
            self.flag = True
            return True
        if m<0 or m>=len(board) or n<0 or n>=len(board[0]) or board[m][n]!=word[cur]:return False
        if self.flag==False:
            c = board[m][n]
            board[m][n] = '.'
            ret1 = self.dfs(board,m+1,n,word,cur+1)
            ret2 = self.dfs(board,m-1,n,word,cur+1)
            ret3 = self.dfs(board,m,n+1,word,cur+1)
            ret4 = self.dfs(board,m,n-1,word,cur+1)
            board[m][n] = c
            return ret1 or ret2 or ret3 or ret4
        else:
            return True
