direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def dfs(grid, visit, x, y):

    for offsetX, offsetY in direction:
        baseX = x + offsetX
        baseY = y + offsetY
        if baseX < 0 or baseY < 0 or baseX >= len(grid) or baseY >= len(grid[0]):
            continue
        if grid[baseX][baseY] == 1 and not visit[baseX][baseY]:
            visit[baseX][baseY] = True
            dfs(grid, visit, baseX, baseY)

    return


row, col = map(int, input().split(" "))

# 邻接矩阵
grid = []
for i in range(row):
    grid.append(list(map(int, input().split(" "))))


visit = [[False] * col for _ in range(row)]

res = 0
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1 and not visit[i][j]:
            res += 1
            print(res)
            dfs(grid, visit, i, j)
print(res)
