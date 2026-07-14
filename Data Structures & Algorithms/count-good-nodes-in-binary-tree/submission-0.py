# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        A node is "good" if there is no node with a
        greater value on the path from the root to it.

        DFS State:
            Carry the maximum value seen so far
            from the root to the current node.
        """

        def dfs(current_node, maximum_value_seen):
            """
            Returns the number of good nodes
            in the current subtree.
            """

            # Base case
            if not current_node:
                return 0

            # -------------------------------------------------
            # Is the current node good?
            #
            # A node is good if its value is greater than or
            # equal to every value seen so far.
            # -------------------------------------------------
            good_nodes = 0

            if current_node.val >= maximum_value_seen:
                good_nodes = 1

            # Update the maximum value before
            # exploring the children.
            maximum_value_seen = max(
                maximum_value_seen,
                current_node.val
            )

            # Count good nodes in both subtrees.
            good_nodes += dfs(
                current_node.left,
                maximum_value_seen
            )

            good_nodes += dfs(
                current_node.right,
                maximum_value_seen
            )

            return good_nodes

        # Root is always a good node because
        # there are no nodes above it.
        return dfs(root, root.val)