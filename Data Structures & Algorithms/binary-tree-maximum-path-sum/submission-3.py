# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        # Stores the overall maximum path sum
        # Using list so it can be updated inside dfs
        res = [root.val]

        def dfs(root):

            # Base case
            # Null nodes contribute 0 to path sum
            if not root:
                return 0

            # Recursively calculate max path from left subtree
            leftMax = dfs(root.left)

            # Recursively calculate max path from right subtree
            rightMax = dfs(root.right)

            # Ignore negative paths
            # Negative contribution only reduces total sum
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            # Maximum path THROUGH current node
            #
            # This is where BOTH left and right can be used
            #
            #        root
            #       /    \
            #   leftMax rightMax
            #
            # Example:
            # left + root + right
            #
            # Update global maximum answer
            res[0] = max(
                res[0],
                leftMax + rightMax + root.val
            )

            # Return ONLY ONE branch upward
            #
            # Parent cannot take both branches again
            #
            # So return:
            # root + max(left, right)
            return root.val + max(leftMax, rightMax)

        dfs(root)

        return res[0]