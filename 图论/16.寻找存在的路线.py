class UnionFind:
    def __init__(self, size):
        self.father = [0] * size
        for i in range(size):
            self.father[i] = i

    def find(self, u):
        if self.father[u] == u:
            return u
        res = self.find(self.father[u])
        self.father[u] = res
        return res

    def join(self, u, v):
        fatherU = self.find(u)
        fatherV = self.find(v)
        if fatherV != fatherU:
            self.father[fatherU] = fatherV

    def isSame(self, u, v):
        fatherU = self.find(u)
        fatherV = self.find(v)
        return fatherU == fatherV


def main():

    nodeNum, edgeNum = map(int, input().split())
    unionFind = UnionFind(nodeNum)

    edges = []
    for i in range(edgeNum):
        edges.append(list(map(int, input().split())))
        unionFind.join(edges[i][0] - 1, edges[i][1] - 1)

    source, dest = map(int, input().split())

    print(1 if unionFind.isSame(source - 1, dest - 1) else 0)


main()
