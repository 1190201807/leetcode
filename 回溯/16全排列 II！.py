class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.trace(nums, [], result, [False] * len(nums))
        return result

    # def trace(self, nums, path, result, used):
    #     if len(path) == len(nums):
    #         result.append(path[:])
    #         return
    #     for i in range(0, len(nums)):
    #         if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
    #             continue
    #         if used[i] == True:
    #             continue
    #         path.append(nums[i])
    #         used[i] = True
    #         self.trace(nums, path, result, used)
    #         path.pop()
    #         used[i] = False

    def trace(self, nums, path, result, used):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(0, len(nums)):
            if used[i] == True:
                continue
            if i > 0 and used[i - 1] == False and nums[i - 1] == nums[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.trace(nums, path, result, used)
            path.pop()
            used[i] = False
