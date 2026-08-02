# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:  
    # Helper function to check whether two trees are exactly identical
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        # If both nodes are null, trees match till this path
        if not p and not q:
            return True

        # If one node is null and the other is not, trees differ
        if not p or not q:
            return False

        # Current node values must match
        if p.val != q.val:
            return False

        # Recursively check left and right subtrees
        left_tree = self.isSameTree(p.left, q.left)
        right_tree = self.isSameTree(p.right, q.right)

        return left_tree and right_tree

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Empty subRoot is always a subtree
        if not subRoot: return True

        # If root becomes empty, subtree cannot exist
        if not root: return False

        # If current trees match

        if self.isSameTree(root, subRoot):

            return True

        # Check:

        # 1. Current tree matches subRoot

        # 2. OR subtree exists in left subtree

        # 3. OR subtree exists in right subtree

        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )