class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        self.trace(nums, [], res, 0)
        return res

    def trace(self, nums, path, result, startIndex):
        if startIndex >= len(nums):
            return
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            result.append(path[:])
            self.trace(nums, path, result, i + 1)
            path.pop()
