class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxItem = float("-inf")
        curSum = 0
        for i in len(nums):
            curSum = nums[i] + curSum
            if curSum <= 0:
                curSum = 0
            maxItem = max(curSum, maxItem)

        return maxItem
