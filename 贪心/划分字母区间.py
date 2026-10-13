class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, ch in enumerate(s):
            lastIndex[ch] = i
        maxDis = -1
        res = []
        num = 0
        for i in range(len(s)):
            num += 1
            maxDis = max(maxDis, lastIndex[s[i]])
            if i == maxDis:
                res.append(num)
                num = 0
        return res
