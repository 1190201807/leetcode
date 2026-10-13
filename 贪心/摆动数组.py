class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 2:
            return len(nums)

        length = 2
        lastDiff = nums[1] - nums[0]
        for i in range(2, len(nums) - 1):

            curDiff = nums[i + 1] - nums[i]
            if curDiff > 0 and lastDiff > 0 or curDiff < 0 and lastDiff < 0:
                lastDiff = curDiff + lastDiff
                continue
            length += 1
            lastDiff = curDiff
