class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        used = [False] * len(candidates)
        self.travel(candidates, target, 0, [], result, 0, used)
        return result

    def travel(self, candidates, target, curSum, path, result, startIndex, used):
        if curSum == target:
            result.append(path[:])
        if curSum >= target:
            return
        for i in range(startIndex, len(candidates)):
            if (
                i > startIndex
                and not used[startIndex]
                and candidates[i] == candidates[i - 1]
            ):
                continue
            path.append(candidates[i])
            used[i] = True
            self.travel(
                candidates, target, curSum + candidates[i], path, result, i + 1, used
            )
            path.pop()
            used[i] = False
