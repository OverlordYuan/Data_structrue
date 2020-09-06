'''
32. 最长有效括号
给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"
'''
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:return 0
        s = ' '+s
        dp = [0]*len(s)
        max_len = 0
        for i in range(2,len(s)):
            if s[i] == ')':
                if s[i-1] =='(':
                    dp[i] = dp[i-2] + 2
                if s[i-1]==')' and s[i-dp[i-1]-1]=='(':
                   dp[i] = dp[i-1] + dp[i-dp[i-1]-2] + 2
                max_len = max(max_len,dp[i])
        return max_len

if __name__ == '__main__':
    s = "()(())"
    a = Solution()
    RES = a.longestValidParentheses(s)
    print(RES)