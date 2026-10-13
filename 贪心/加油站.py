# 贪心2
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         sum = 0
#         startIndex = -1
#         totalSum = 0
#         for i in range(len(gas)):
#             diff = gas[i] - cost[i]
#             sum += diff
#             totalSum += diff
#             if sum <= 0:
#                 sum = 0
#                 startIndex = -1
#             else:
#                 if startIndex == -1:
#                     startIndex = i
#         if totalSum >= 0:
#             return startIndex
#         else:
#             return -1


# 暴力
# class Solution:
#     def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
#         indexRes = -1
#         for i in range(len(gas)):
#             count = len(gas) - 1
#             startIndex = i
#             total = 0
#             while count >= 0:
#                 total = total + gas[startIndex % len(gas)] - cost[startIndex % len(gas)]
#                 if total < 0:
#                     break
#                 startIndex += 1
#                 count -= 1
#             if total >= 0:
#                 indexRes = i
#         return indexRes


# 贪心1
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        diff = []
        for i in range(len(gas)):
            diff.append(gas[i] - cost[i])

        minItem = float("inf")
        total = 0
        for i in range(len(diff)):
            total += diff[i]
            if total < 0:
                minItem = min(minItem, total)
        if total < 0:
            return -1
        if minItem >= 0:
            return 0
        totalDesc = 0
        for i in range(len(diff) - 1, -1, -1):
            totalDesc += diff[i]
            if totalDesc + minItem >= 0:
                return i
        return -1
