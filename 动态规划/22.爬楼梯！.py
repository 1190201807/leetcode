n, m = map(int, input().split())
# dp = [[0 for _ in range(n + 1)] for _ in range(m)]
# for i in range(m):
#     dp[i][0] = 1

# for j in range(1, n + 1):
#     for i in range(0, m):
#         if j - i - 1 >= 0:
#             dp[i][j] += dp[m - 1][j - i - 1]
#         if i - 1 >= 0:
#             dp[i][j] += dp[i - 1][j]

# print(dp[m - 1][n])

dp = [0 for _ in range(n + 1)]
dp[0] = 1
for j in range(1, n + 1):
    for i in range(0, m):
        if j - i - 1 >= 0:
            dp[j] += dp[j - i - 1]
print(dp)
print(dp[n])
