class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[0] * (2 * k + 1) for _ in range(len(prices))]
        for i in range(2 * k + 1):
            if i % 2 == 1:
                dp[0][i] = -prices[0]

        for i in range(1, len(prices)):
            for j in range(0, k + 1):
                if j == 0:
                    dp[i][0] = 0
                else:
                    dp[i][2 * j] = max(
                        dp[i - 1][2 * j - 1] + prices[i], dp[i - 1][2 * j]
                    )
                    dp[i][2 * j - 1] = max(
                        dp[i - 1][2 * j - 2] - prices[i], dp[i - 1][2 * j - 1]
                    )
        return dp[len(prices) - 1][2 * k]
