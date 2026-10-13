class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = [[0 for _ in range(target + 1)] for _ in range(len(nums))]
        for i in range(target):
            if i < nums[0]:
                dp[0][i] = 0
            else:
                dp[0][i] = nums[0]
        for i in range(1, len(nums)):
            for j in range(0, target + 1):
                if j - nums[i] >= 0:
                    dp[i][j] = max(
                        dp[i][j], dp[i - 1][j - nums[i]] + nums[i], dp[i - 1][j]
                    )
                else:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j])

        print(dp)

        return dp[len(nums) - 1][target] == target
