v, e = map(int, input().split())

grid = [[float("inf")] * (v + 1) for _ in range(v + 1)]
for i in range(e):
    s, d, val = map(int, input().split(" "))
    grid[s][d] = val

visit = [False] * (v + 1)
minDisList = [float("inf")] * (v + 1)

minDisList[1] = 0
path = [i for i in range(v + 1)]

for loop in range(1, v + 1):
    minIndex = -1
    minDis = float("inf")
    for i in range(1, v + 1):
        if not visit[i] and minDisList[i] < minDis:
            minIndex = i
            minDis = minDisList[i]
    visit[minIndex] = True

    for i in range(1, v + 1):
        if not visit[i]:
            if minDis + grid[minIndex][i] < minDisList[i]:
                minDisList[i] = minDis + grid[minIndex][i]
                path[i] = minIndex

print(minDisList[v] if minDisList[v] != float("inf") else -1)
