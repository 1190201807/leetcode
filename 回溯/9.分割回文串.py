class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.trace(s, result, [], 0)
        return result

    def trace(self, s, result, path, startIndex):
        if startIndex >= len(s):
            result.append(path)
        for i in range(startIndex, len(s)):
            if self.isHuiWen(s[startIndex : i + 1]):
                path.append(s[startIndex : i + 1])
                self.trace(s, result, path, i + 1)
                path.pop()
            else:
                break

    def isHuiWen(self, s):
        i = 0
        j = len(s) - 1
        flag = True
        while i < j:
            if s[i] != s[j]:
                flag = False
                break
            i += 1
            j -= 1
        return flag
