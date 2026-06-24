class Solution:
    def diameterOfBinaryTree(
        self,
        root: Optional[TreeNode]
    ) -> int:

        # Stores maximum diameter found so far
        self.maximum_diameter = 0

        def calculate_height(node):
            """
            Returns:

                Height of subtree rooted at node

            While returning height,
            also updates diameter.
            """

            # Empty subtree has height 0
            if not node:
                return 0

            # Height of left subtree
            left_subtree_height = (
                calculate_height(node.left)
            )

            # Height of right subtree
            right_subtree_height = (
                calculate_height(node.right)
            )

            # Diameter passing through current node
            #
            # Longest path:
            #
            # left subtree
            #      +
            # right subtree
            diameter_through_current_node = (
                left_subtree_height
                +
                right_subtree_height
            )

            self.maximum_diameter = max(
                self.maximum_diameter,
                diameter_through_current_node
            )

            # Return height to parent
            return (
                1
                +
                max(
                    left_subtree_height,
                    right_subtree_height
                )
            )

        calculate_height(root)

        return self.maximum_diameter