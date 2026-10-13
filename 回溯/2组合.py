# https://leetcode.cn/problems/combinations/


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.trace(result, [], n, k, 1)
        return result

    def trace(self, result, path, n, k, startIndex):
        if len(path) >= k:
            result.append(path[:])
        for i in range(startIndex, n + 1):
            if k - len(path) > n - i + 1:
                break
            path.append(i)
            self.trace(result, path, n, k, i + 1)
            path.pop()
