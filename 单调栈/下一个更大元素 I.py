class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict = {}
        for i in range(len(nums1)):
            dict[nums1[i]] = i
        stack = []
        stack.append(0)
        res = [-1] * len(nums1)
        for i in range(1, len(nums2)):
            while len(stack) > 0 and nums2[i] > nums2[stack[-1]]:
                if nums2[stack[-1]] in nums1:
                    res[dict[nums2[stack[-1]]]] = nums2[i]
                stack.pop()
            stack.append(i)
            nums1.sort(key=lambda x: x[0])
        return res
