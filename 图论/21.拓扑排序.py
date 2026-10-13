from collections import defaultdict

vNum, ENum = map(int, input().split())

inDegree = [0] * vNum
dict = defaultdict(list)

for i in range(ENum):
    s, d = map(int, input().split())
    dict[s].append(d)
    inDegree[d] += 1

queue = []
visit = [False] * vNum

for i in range(ENum):
    if inDegree[i] == 0:
        queue.append(i)
        visit[i] = True

# queue =[x for x in range(ENum) if inDegree[x] == 0]

res = []
while len(queue) > 0:
    head = queue[0]
    res.append(head)
    del queue[0]
    for node in dict[head]:
        if not visit[node]:
            inDegree[node] -= 1
            if inDegree[node] == 0:
                queue.append(node)
                visit[node] = True

if len(res) == vNum:
    print(" ".join(map(str, res)))
else:
    print(-1)
