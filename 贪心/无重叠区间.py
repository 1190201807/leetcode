class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        startIndex = float("inf")
        endIndex = float("-inf")
        intervals.sort(key=lambda x: x[0])
        res = 0
        for interval in intervals:
            if interval[0] >= startIndex and interval[0] < endIndex:
                res += 1

                if interval[1] < endIndex:
                    startIndex = interval[0]
                    endIndex = interval[1]
            else:
                startIndex = interval[0]
                endIndex = interval[1]
        return res
