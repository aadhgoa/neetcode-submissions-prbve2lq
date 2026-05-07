# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Every node should swap its left and right child.
"""
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # ---------------------------------------------------

        # Base Case

        # If node is None, nothing to invert

        # ---------------------------------------------------

        if not root:

            return None

        # ---------------------------------------------------

        # Swap left and right children

        # ---------------------------------------------------

        root.left, root.right = root.right, root.left

        # ---------------------------------------------------

        # Recursively invert left subtree

        # ---------------------------------------------------

        self.invertTree(root.left)


         # ---------------------------------------------------

        # Recursively invert right subtree

        # ---------------------------------------------------

        self.invertTree(root.right)


        # Return the root after inversion

        return root