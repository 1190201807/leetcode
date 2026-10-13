class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i - j] * j, dp[i], (i - j) * j)

        return dp[n]
