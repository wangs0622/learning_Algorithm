'''
Created on 2018年3月24日

@author: wangs0622

剑指 offer 19 题，正则表达式匹配问题

'''
# 按照书上的代码思路写的程序
def match(string, pattern):
    print(string, '   ', pattern)
    
    
    if len(pattern) == 0:
        if len(string) == 0:
            return True
        else:
            return False
    if len(pattern) == 1:
        if len(string) != 1: return False
        else:
            if string == pattern or pattern == '.':
                return True
    if len(string) == 0:
        if len(pattern) != 2:
            return False
        else:
            if pattern[1] == '*':
                return False
            else:
                return False
   
    if pattern[1] == '*':
        if pattern[0] == string[0] or (pattern[0] == '.' and len(string) > 0):
            return match(string[1:], pattern[2:]) or \
                    match(string[1:], pattern) or \
                    match(string, pattern[2:])
        else:
            return match(string, pattern[2:])
    if string[0] == pattern[0] or (pattern[0] == '.' and len(string) != 0):
        return match(string[1:], pattern[1:])
    return False

#---------------------------leetcode 上遇到过的相同的问题-------------------------------

# 参考地址： https://leetcode.com/problems/regular-expression-matching/solution/
#----------------------------------------------------------------------------
# method 1： 递归调用方法
import numpy as np
class Solution:
    def isMatchWithoutStar(self, s, p):
        '''
        function: 首先考虑一下简单的情况，那就是没有 * 的情况。
        function: 此函数作用是假设 p 中不包含通用字符 * 时， 两个字符串的匹配情况
        '''
        # 之所以 以 not p 作为判断条件，是因为：
        # 1. 当 len(p) > len(s) 时，这句话还没执行时，下面的 bool(s) 就会得到一个 False，最终结果为 False 
        # 2. 当 len(p) < len(s) 时， 当 p 为空时，此处返回 False，得到最后结果为 False
        # 3. 当 len(p) = len(s) 时，此处返回值为 True
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        return first_match and self.isMatchWithoutStar(s[1:], p[1:])
    
    def isMatchSec(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        :function: 使用递归的方法解决问题
        """
        if not p: return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return (first_match and self.isMatch(s[1:], p)) or (self.isMatch(s, p[2:]))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    def isMatchDY(self,s,p):
        '''
        :type s: str
        :type p: str
        :rtype: bool
        :function: 使用动态规划解决问题. 首先，dp[i,j] 代表了 s[i:] 与 p[j:] 的是否匹配情况
        : 则可知， s[len(s):] = '' , p[len(p):]='' 两者匹配。我们想要的结果为 dp[0,0] 的值。
        : 分析可知， dp[:,len(p)] 的值全部为 False, 除过 dp[-1, -1]。 
        : 我们需要我们的 dp 矩阵的第二个维度的索引值最大为： len(p)，所以它应该有 len(p)+1列数； 同理对于行
        : 现在我想知道的是 dp[i,j] 等于什么。要分情况：
        : 当 j + 1 = len(p) 时，即 p 中只有一个字符，肯定不会是 * ,其结果（倒数第二列） 取决于
        :     第一个值的匹配情况  与 dp[i+1,j+1] 的与值。
        : 当 j + 1 < len(p) 的时候，即 p 中至少有两个字符，这个时候，可能存在 * 。 
        : 当 p 中的第二个字符就是 * 的时候，分两种情况:
        :     第一种，不考虑第一个值的匹配情况， dp[i,j] = dp[i,j+2]
        :     第二种情况： 考虑第一个值的匹配情况，其值为 first_match and dp[i+1,j] 
        : 当   p 中的第二个字符不是 * 的时候
        :     dp[i][j] = first_match and dp[i+1][j+1]
        '''
        dp = np.zeros((len(s)+1, len(p)+1), dtype=bool)
        #print("dp.shape: ", dp.shape)
        dp[-1][-1] = True
        for i in range(len(s), -1, -1):
            for j in range(len(p)-1, -1, -1):
                first_match = i<len(s) and p[j] in {'.', s[i]}
                if j+1<len(p) and p[j+1]=="*":
                    #print("i,j: ",i,j)
                    dp[i][j] = dp[i][j+2] or (first_match and dp[i+1][j])
                else:
                    dp[i][j] = first_match and dp[i+1][j+1]
        return dp[0][0]
    
    
    def isMatchDY2(self,s,p):      
        '''
        :type s: str
        :type p: str
        :rtype: bool
        : 思想与前面的一样，此处采用的是递归的思想
        '''
        memary = {}
        def dp(i,j):
            if (i,j) in memary:
                return memary[i,j]
            else:
                if j == len(p): memary[i,j] = (i==len(s))
                else:
                    first_match = (i<len(s)) and (p[j] in {'.', s[i]})
                    if j+1 < len(p) and p[j+1]=='*':
                        memary[i,j] = dp(i,j+2) or first_match and dp(i+1,j)
                    else:
                        memary[i,j] = first_match and dp(i+1,j+1)
                        
            return memary[i,j]
        
        
        return dp(0,0)

if __name__ == '__main__':
    string = 'aaa.......xxxbbbbacccceeea'
    pattern = 'a*.*.*b*ac*.*a'
    print(match(string, pattern))
             
        