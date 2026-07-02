# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if node is None:
                return 0
            left=depth(node.left)
            right=depth(node.right)
            if node.left is None:
                return 1+right
            if node.right is None:
                return 1+left
            return 1+min(left,right)
        return depth(root)