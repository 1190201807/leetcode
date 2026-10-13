import heapq

v, e = map(int, input().split(" "))

grid = [[float("inf")] * (v + 1) for _ in range(v + 1)]
for i in range(e):
    s, d, val = map(int, input().split(" "))
    grid[s][d] = val

visit = [False] * (v + 1)
minDisList = [float("inf")] * (v + 1)

minDisList[1] = 0
visit[1] = True
path = [i for i in range(v + 1)]
pq = []
heapq.heappush(pq, [0, 1])
while len(pq) > 0:
    curVal, curIndex = heapq.heappop(pq)
    visit[curIndex] = True
    for i in range(1, v + 1):
        if not visit[i] and minDisList[i] > curVal + grid[curIndex][i]:
            minDisList[i] = curVal + grid[curIndex][i]
            heapq.heappush(pq, [minDisList[i], i])
            path[i] = curIndex

# print(path)
print(-1 if minDisList[v] == float("inf") else minDisList[v])
