# https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 1 and s == "0": return 0
        if n < 2: return 1
        dp = [0] * (n+1)
        dp[-1] = 1
        if s[-1] != "0": dp[-2] = 1
        for i in range(n-2, -1, -1):
            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i+1]
            if 10 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i+2]
        return dp[0]
