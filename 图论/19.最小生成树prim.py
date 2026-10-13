nodeNum, edgeNum = map(int, input().split(" "))

grid = [[float("inf")] * (nodeNum + 1) for _ in range(nodeNum + 1)]

for i in range(edgeNum):
    s, d, val = map(int, input().split(" "))
    grid[s][d] = val
    grid[d][s] = val

minDisList = [float("inf")] * (nodeNum + 1)
visit = [False] * (nodeNum + 1)
lastVisitIndex = 1
visit[lastVisitIndex] = True
sum = 0
path = [x for x in range(nodeNum + 1)]

for i in range(0, nodeNum - 1):
    minIndex = 1
    minDis = float("inf")
    for v in range(1, nodeNum + 1):
        if not visit[v]:
            if minDisList[v] > grid[v][lastVisitIndex]:
                minDisList[v] = grid[v][lastVisitIndex]
                path[v] = lastVisitIndex

            if minDisList[v] < minDis:
                minDis = minDisList[v]
                minIndex = v
    sum += minDisList[minIndex]

    lastVisitIndex = minIndex
    visit[minIndex] = True

print(path)
print(sum)
