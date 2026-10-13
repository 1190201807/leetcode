# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    NO_COVER = 3
    COVER = 2
    CAMERA = 1
    res = 0

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        head = self.trace(root)
        if head == self.NO_COVER:
            self.res += 1
        return self.res

    def trace(self, root):
        if root == None:
            return self.COVER
        l = self.trace(root.left)
        r = self.trace(root.right)
        if l == self.NO_COVER or r == self.NO_COVER:
            self.res += 1
            return self.CAMERA
        if (
            l == self.CAMERA
            and r == self.COVER
            or r == self.CAMERA
            and l == self.COVER
            or l == self.CAMERA
            and r == self.CAMERA
        ):
            return self.COVER
        if r == self.COVER and l == self.COVER:
            return self.NO_COVER


# https://leetcode.cn/problems/binary-tree-cameras/submissions/720420648/
