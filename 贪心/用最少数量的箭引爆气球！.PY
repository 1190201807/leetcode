class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0]))
        res = 0
        startIndex = float("inf")
        endIndex = float("-inf")
        for point in points:

            if point[0] >= startIndex and point[0] <= endIndex:
                startIndex = max(startIndex, point[0])
                endIndex = min(endIndex, point[1])
            else:
                startIndex = point[0]
                endIndex = point[1]
                res += 1
        return res
