class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.trace(nums, [], result, 0)
        return result

    def trace(self, nums, path, result, startIndex):
        if len(path) >= 2:
            result.append(path[:])
        _set = set()
        for i in range(startIndex, len(nums)):
            if nums[i] in _set or not (len[path] > 0 and nums[i] < path[-1]):
                continue
            path.append(nums[i])
            _set.add(nums[i])
            self.trace(nums, path, result, i + 1)
            path.pop()
