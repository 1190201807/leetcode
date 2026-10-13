class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        stack.append(0)
        res = 0
        for i in range(1, len(height)):
            while len(stack) > 0 and height[i] >= height[stack[-1]]:
                curHeight = height[stack[-1]]
                stack.pop()
                if len(stack) > 0:
                    res += (min(height[stack[-1]], height[i]) - curHeight) * (
                        i - stack[-1] - 1
                    )

            stack.append(i)
        return res
