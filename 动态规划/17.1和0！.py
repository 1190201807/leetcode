class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [
            [[0 for _ in range(n + 1)] for _ in range(m + 1)] for _ in range(len(str))
        ]
        num0 = self.findNum(strs[0], "0")
        num1 = self.findNum(strs[0], "1")
        for j in range(m + 1):
            for k in range(n + 1):
                if j >= num0 and k >= num1:
                    dp[0][j][k] = 1
        for i in range(1, len(strs)):
            _num0 = self.findNum(strs[i], "0")
            _num1 = self.findNum(strs[i], "1")
            for j in range(m + 1):
                for k in range(n + 1):
                    if j - _num0 >= 0 and k - _num1 >= 0:
                        dp[i][j][k] = max(
                            dp[i - 1][j - _num0][k - _num1] + 1, dp[i - 1][j][k]
                        )
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]

        return dp[len(strs) - 1][m][n]

    def findNum(self, str, tar):
        res = 0
        for i in range(0, len(str)):
            if str[i] == tar:
                res += 1
        return res
