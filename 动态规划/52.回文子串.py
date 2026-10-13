class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        sum = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(0, len(s)):
                if i > j:
                    continue
                if i == j:
                    dp[i][j] = True
                    sum += 1
                elif j - i == 1:
                    if s[i] == s[j]:
                        sum += 1
                        dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        sum += 1
                        dp[i][j] = dp[i + 1][j - 1]

        return sum
