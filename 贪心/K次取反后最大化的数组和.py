class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x: abs(x), reverse=True)  # 第一步：按照绝对值降序排序数组A
        nums.sort(key=lambda x:())
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1
            if k == 0:
                break
        if k > 0:
            if k % 2 == 1:
                nums[len(nums) - 1] = -nums[len(nums) - 1]
        result = sum(nums)
        return result
