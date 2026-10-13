class UnionFindSet:
    father = []
    size = 0

    def find(self, a):
        fatherA = a
        while self.father[fatherA] != fatherA:
            fatherA = self.father[fatherA]
        self.father[a] = fatherA
        return a

    def join(self, a, b):
        fatherA = self.find(a)
        fatherB = self.find(b)
        if fatherA != fatherB:
            self.father[fatherA] = fatherB

    def isSame(self, a, b):
        fatherA = self.find(a)
        fatherB = self.find(b)
        return fatherA == fatherB

    def __init__(self, num) -> None:
        self.size = num
        for i in range(num):
            self.father[i] = i


nodeNum, edgeNum = map(int, input().split(" "))
unionset = UnionFindSet(nodeNum)
for _ in range(edgeNum):
    s, d = map(int, input().split(" "))
    unionset.join(s, d)
source, dest = map(int, input().split(" "))
if unionset.isSame(source, dest):
    print(1)
print(0)
