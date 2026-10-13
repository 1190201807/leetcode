class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxDis = 0
        for i in range(len(nums)):
            if i <= maxDis:
                maxDis = max(maxDis, i + nums[i])
                if maxDis >= len(nums) - 1:
                    return True
            else:
                return False
        return True
