class UnionFind:

    def __init__(self, size):
        self.father = [x for x in range(size + 1)]

    def find(self, u):
        if self.father[u] == u:
            return u
        root = self.find(self.father[u])
        self.father[u] = root
        return root

    def join(self, u, v):
        fu = self.find(u)
        fv = self.find(v)
        if fu != fv:
            self.father[fu] = fv

    def isSame(self, u, v):
        return self.find(u) == self.find(v)


vNum, edgeNum = map(int, input().split(" "))

unionFind = UnionFind(vNum)
edges = []
for i in range(edgeNum):
    edges.append(list(map(int, input().split(" "))))

edges.sort(key=lambda x: x[2])

loop = 0
sum = 0
path = [x for x in range(vNum)]
for s, d, val in edges:
    if loop > vNum - 1:
        break
    if not unionFind.isSame(s, d):
        sum += val
        path[s] = d
        unionFind.join(s, d)
        loop += 1
print(path)
print(sum)
