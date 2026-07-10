from collections import deque


class Solution:
    def levelOrder(
        self,
        root: Optional[TreeNode]
    ) -> List[List[int]]:
        """
        Perform a Breadth First Search (BFS).

        Process one tree level at a time.

        Queue stores all nodes of the
        current and upcoming levels.
        """

        # Empty tree
        if not root:
            return []

        result = []

        # BFS queue
        queue = deque([root])

        while queue:

            # Number of nodes
            # in the current level
            level_size = len(queue)

            current_level = []

            # Process every node
            # in the current level
            for _ in range(level_size):

                current_node = queue.popleft()

                current_level.append(current_node.val)

                # Add children
                # for the next level
                if current_node.left:
                    queue.append(current_node.left)

                if current_node.right:
                    queue.append(current_node.right)

            # Store current level
            result.append(current_level)

        return result