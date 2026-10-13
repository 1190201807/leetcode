direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]


def dfs(grid, visit, x, y, result):
    visit[x][y] = True
    result.add((x, y))

    for i, j in direction:
        x1 = i + x
        y1 = j + y
        if x1 < 0 or y1 < 0 or x1 >= len(grid) or y1 >= len(grid[0]):
            continue
        if grid[x1][y1] >= grid[x][y] and visit[x1][y1] == False:
            dfs(grid, visit, x1, y1, result)


row, col = map(int, input().split(" "))

grid = []

for i in range(row):
    grid.append(list(map(int, input().split(" "))))

firstVisit = [[False] * col for _ in range(row)]
firstRes = set()
secondVisit = [[False] * col for _ in range(row)]
secondRes = set()

for i in range(row):
    dfs(grid, firstVisit, i, 0, firstRes)
    dfs(grid, secondVisit, i, col - 1, secondRes)

for i in range(col):

    dfs(grid, firstVisit, 0, i, firstRes)
    dfs(grid, secondVisit, row - 1, i, secondRes)

res = firstRes & secondRes
for i, j in res:
    print(f"{i} {j}")
