# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         deep = [False] * len(nums)
#         result = [[]]
#         self.trace(nums, [], result, deep, 0)
#         return result

#     def trace(self, nums, path, result, deep, startIndex):
#         for i in range(startIndex, len(nums)):
#             if i > 0 and nums[i] == nums[i - 1] and deep[i - 1] == False:
#                 continue
#             deep[i] = True
#             path.append(nums[i])
#             result.append(path[:])
#             self.trace(nums, path, result, deep, i + 1)
#             path.pop()
#             deep[i] = False


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False] * len(nums)
        self.trace(nums, [], result, 0, used)
        return result

    def trace(self, nums, path, result, startIndex, used):
        for i in range(startIndex, len(nums)):
            if i > 0 and nums[i] == nums[i - 1] and used[i - 1] == False:
                continue
            used[i] = True
            path.append(nums[i])
            result.append(path[:])
            self.trace(nums, path, result, i + 1, used)
            used[i] = False
            path.pop()
