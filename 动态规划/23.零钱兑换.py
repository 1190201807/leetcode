class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(len(coins)):
            for j in range(1, amount + 1):
                if j - coins[i] >= 0:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        return -1 if dp[amount] == float("inf") else dp[amount]
