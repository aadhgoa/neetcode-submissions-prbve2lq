# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Compare 2 trees Value-by-Value recursively
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # ---------------------------------------------------

        # Case 1:

        # Both nodes are None

        # Trees match till this point

        # ---------------------------------------------------
        if not p and not q:
            return True

        # ---------------------------------------------------

        # Case 2:

        # One node is None and the other isn't

        # Structure mismatch

        # ---------------------------------------------------
        if not p or not q:
            return False


        # ---------------------------------------------------

        # Case 3:

        # Node values differ

        # ---------------------------------------------------
        if p.val != q.val:
            return False

        # ---------------------------------------------------

        # Recursively compare:

        # 1. Left subtrees

        # 2. Right subtrees

        # ---------------------------------------------------
        left_same = self.isSameTree(p.left, q.left)
        right_same = self.isSameTree(p.right, q.right)

        return left_same and right_same