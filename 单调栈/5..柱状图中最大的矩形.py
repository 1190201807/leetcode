class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = []
        stack.append(0)
        res = 0
        for i in range(1, len(heights)):
            while len(stack) > 0 and heights[stack[-1]] > heights[i]:
                curIndex = stack[-1]
                stack.pop()
                res = max(res, heights[curIndex] * (i - 1 - stack[-1]))

            stack.append(i)
        return res
