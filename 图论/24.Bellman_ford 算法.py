v, e = map(int, input().split(" "))

edges = []

for i in range(e):
    edges.append(list(map(int, input().split(" "))))

minDis = [float("inf")] * (v + 1)
minDis[1] = 0

for i in range(v - 1):
    updated = False
    for s, d, val in edges:
        if minDis[s] != float("inf"):
            if minDis[s] + val < minDis[d]:
                minDis[d] = minDis[s] + val
                updated = True
    if updated == False:
        break


print(minDis[v] if minDis[v] != float("inf") else "unconnected")
