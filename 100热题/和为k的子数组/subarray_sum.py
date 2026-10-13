class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sumArr = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            sumArr[i + 1] = sumArr[i] + nums[i]
        res = 0
        map = dict()
        map[0] = 1
        for i in range(1, len(sumArr)):
            if sumArr[i] - k in map:
                res += map[sumArr[i] - k]
            if sumArr[i] in map:
                map[sumArr[i]] += 1
            else:
                map[sumArr[i]] = 1
        return res
