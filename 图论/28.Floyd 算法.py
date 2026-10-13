v, e = map(int, input().split(" "))

grid = [[float("inf")] * (v + 1) for _ in range(v + 1)]
for i in range(e):
    s, d, val = map(int, input().split(" "))
    grid[d][s] = val
    grid[s][d] = val

resNum = int(input())

resSet = []

for _ in range(resNum):
    s, d = map(int, input().split(" "))
    resSet.append([s, d])

dp = [[[float("inf")] * (v + 1) for _ in range(v + 1)] for _ in range(v + 1)]

for i in range(1, v + 1):
    for j in range(1, v + 1):
        dp[i][j][0] = grid[i][j]

for k in range(1, v + 1):
    for i in range(1, v + 1):
        for j in range(1, v + 1):
            dp[i][j][k] = min(dp[i][j][k - 1], dp[i][k][k - 1] + dp[k][j][k - 1])

for s, d in resSet:
    print(-1 if dp[s][d][v] == float("inf") else dp[s][d][v])
