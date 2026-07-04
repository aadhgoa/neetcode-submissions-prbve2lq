# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        A binary tree is balanced if, for every node,

            |left subtree height - right subtree height| <= 1

        DFS Contract:

        Return:
            Height of the subtree  -> if it is balanced

            -1                     -> if it is NOT balanced

        Once -1 is returned,
        it propagates all the way back up the recursion.
        """

        def getHeight(node):
            """
            Returns:

                Height of subtree  -> Balanced subtree

                -1                 -> Unbalanced subtree
            """

            # Empty subtree
            #
            # Height = 0
            if not node:
                return 0

            # Compute left subtree height
            left_subtree_height = getHeight(node.left)

            # Left subtree already unbalanced
            # No need to continue.
            if left_subtree_height == -1:
                return -1

            # Compute right subtree height
            right_subtree_height = getHeight(node.right)

            # Right subtree already unbalanced
            if right_subtree_height == -1:
                return -1

            # Current node becomes unbalanced
            #
            # Example:
            #
            # Left Height  = 3
            # Right Height = 1
            #
            # Difference = 2
            if abs(
                left_subtree_height
                - right_subtree_height
            ) > 1:
                return -1

            # Current subtree is balanced.
            #
            # Return its height to the parent.
            return (
                1
                + max(
                    left_subtree_height,
                    right_subtree_height
                )
            )

        # Tree is balanced
        # if DFS never returned -1.
        return getHeight(root) != -1