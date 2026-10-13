# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         intervals.sort(key=lambda x: (x[0]))
#         res = []
#         startIndex = intervals[0][0]
#         endIndex = intervals[0][1]
#         for i in range(1, len(intervals)):
#             interval = intervals[i]
#             if interval[0] >= startIndex and interval[0] <= endIndex:
#                 startIndex = min(startIndex, interval[0])
#                 endIndex = max(endIndex, interval[1])
#             else:
#                 res.append([startIndex, endIndex])
#                 startIndex = interval[0]
#                 endIndex = interval[1]
#         res.append([startIndex, endIndex])
#         return res


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] >= res[-1][0] and interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        return res
