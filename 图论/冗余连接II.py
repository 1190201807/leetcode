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


def isTree(num, edges, excludeEdgeIndex):
    unionFind = UnionFind(num)
    for i in edges:
        if i == excludeEdgeIndex:
            continue
        if unionFind.isSame(edges[i][0], edges[i][1]):
            return False
        unionFind.join(edges[i][0], edges[i][1])
    return True


from collections import defaultdict


def main():
    num = int(input())
    unionFind = UnionFind(num)
    edges = []
    indegree = defaultdict(int)
    inDegreeEdge = []
    for i in range(num):
        s, d = map(int, input().split())
        edges.append([s, d])
        indegree[d - 1] += 1
    for i in range(num):
        source, dest = edges[i]
        if indegree[dest - 1] == 2:
            inDegreeEdge.append(i)
    if len(inDegreeEdge) == 2:
        for i in range(1, -1, -1):
            if isTree(num, edges, inDegreeEdge[i]):
                print(edges[inDegreeEdge[i]][0], edges[inDegreeEdge[i]][1])
            else:
                print(edges[inDegreeEdge[0]][0], edges[inDegreeEdge[0]][1])
            return
    else:
        for s, d in edges:
            if unionFind.isSame(s, d):
                print(s, d)
                return
            unionFind.join(s, d)


main()
