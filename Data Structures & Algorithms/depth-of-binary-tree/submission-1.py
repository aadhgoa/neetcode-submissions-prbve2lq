# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
The longest path from root → deepest leaf
"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # ---------------------------------------------------

        # Base Case:

        # Empty tree has depth 0

        # ---------------------------------------------------
        if root is None:
            return 0

        # ---------------------------------------------------

        # Recursively calculate left subtree depth

        # ---------------------------------------------------
        left_depth = self.maxDepth(root.left)


        # ---------------------------------------------------

        # Recursively calculate right subtree depth

        # ---------------------------------------------------
        right_dept = self.maxDepth(root.right)


        # ---------------------------------------------------

        # Current node depth =

        # 1 + maximum of left/right depths

        # ---------------------------------------------------
        return 1 + max(left_depth, right_dept)
