class Solution:
    def jump(self, nums: List[int]) -> int:
        maxLength = 0
        curLength = 0
        count = 0
        for i in range(len(nums)):
            if maxLength >= len(nums) - 1:
                count += 1
                return count
            maxLength = max(maxLength, nums[i] + i)
            if curLength == i:
                count += 1
                curLength = maxLength
        return count


# class Solution:
# def jump(self, nums: List[int]) -> int:
#     count = 1
#     for i in range(len(nums)):
#         if nums[i] + i >= len(nums) - 1:
#             return count
#         i = self.findMax(i, nums[i] + i, nums)
#         count += 1
#     return count

# def findMax(self,start, end, nums):
#     maxIndex = -1
#     maxDis = 0
#     for i in range(start, end + 1):
#         if nums[i] + i > maxDis:
#             maxDis = nums[i] + i
#             maxIndex = i

#     return maxIndex


# 动态规划
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float("inf")] * len(nums)
        dp[0] = 0
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[j] + j >= i:
                    dp[i] = min(dp[j] + 1, dp[i])
        return dp[len(nums) - 1]
