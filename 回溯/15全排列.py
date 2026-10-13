class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.trace(nums, [], result, [False] * len(nums))
        return result

    def trace(self, nums, path, result, used):
        if len(path) == len(nums):
            result.append(path[:])
        for i in range(0, len(nums)):
            if used[i] == True:
                continue
            used[i] = True
            path.append(nums[i])
            self.trace(nums, path, result, used)
            path.pop()
            used[i] = False
