class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []
        # 固定i
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if nums[j] + nums[k] + nums[i] > 0:
                    k = k - 1

                elif nums[j] + nums[k] + nums[i] < 0:

                    j = j + 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j = j + 1
                    k = k - 1
                    while nums[j] == nums[j - 1] and j < k:
                        j = j + 1
                    while nums[k] == nums[k + 1] and j < k:
                        k = k - 1
        return res
