class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.travel(candidates, target, 0, [], result, 0)
        return result

    def travel(self, candidates, target, curSum, curPath, result, startIndex):
        if curSum == target:
            result.append(curPath[:])
            return
        if curSum > target:
            return
        for i in range(startIndex, len(candidates)):
            curPath.append(candidates[i])
            self.travel(candidates, target, curSum + candidates[i], curPath, result, i)
            curPath.pop()
