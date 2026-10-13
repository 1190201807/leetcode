# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         i = 0
#         j = 0
#         sum = 0
#         res = len(nums)
#         while i < len(nums) and j < len(nums):
#             sum = sum + nums[i]
#             while sum > target and j <= i:
#                 sum = sum - nums[j]
#                 j = j + 1

#             if sum == target:
#                 res = min(i - j + 1, res)
#             i = i + 1

#         return res


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum = nums[0]
        res = float("inf")
        j = 0
        for i in range(1, len(nums)):
            sum += nums[i]
            while sum >= target:
                res = min(res, i - j + 1)
                sum -= nums[j]
                j += 1
        return 0 if res == float("inf") else res
