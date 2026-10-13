direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(grid, visit, x, y):
    que = []

    que.append([x, y])

    while len(que) > 0:
        curX, curY = que[0]
        del que[0]
        for offsetX, offsetY in direction:
            _x = curX + offsetX
            _y = curY + offsetY
            if _x < 0 or _y < 0 or _x >= len(grid) or _y >= len(grid[0]):
                continue
            if grid[_x][_y] == 1 and not visit[_x][_y]:
                visit[_x][_y] = True
                que.append([_x, _y])


row, col = map(int, input().split(" "))

grid = []
for i in range(row):
    grid.append(list(map(int, input().split(" "))))

res = 0
visit = [[False] * col for _ in range(row)]
for i in range(row):
    for j in range(col):
        if grid[i][j] == 1 and not visit[i][j]:
            res += 1
            visit[i][j] = True
            bfs(grid, visit, i, j)
print(res)
