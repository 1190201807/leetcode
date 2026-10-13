class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.trace(k, n, 1, [], 0, result)
        return result

    def trace(self, deep, sum, startIndex, path, curSum, result):
        if len(path) == deep:
            if curSum == sum:
                result.append(path[:])
            return
        for i in range(startIndex, 11):
            if deep - len(path) > 11 - i or curSum + i > sum:
                break
            path.append(i)
            self.trace(deep, sum, i + 1, path, curSum + i, result)
            path.pop()
