'''
5. 最长回文子串
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
示例 1：
输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：
输入: "cbbd"
输出: "bb"
'''
class Solution(object):
    def longestPalindrome(self, s):
        if len(s)<2:return s
        dp = [([False] * len(s)) for i in range(len(s))]
        begin = 0
        max_len = 0
        for i in range(1,len(s)):
            for j in range(i):
                if s[i]==s[j] and ((i-j)<3 or dp[i-1][j+1]==True):
                    dp[i][j] = True
                    if (i-j)>max_len:
                        max_len = i-j
                        begin = j
        return s[begin:begin+max_len+1]

if __name__ == '__main__':
    a  = Solution()
    s = "babad"
    res = a.longestPalindrome(s)
    print(res)