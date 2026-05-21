# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        # Stores the final right side view
        res = []

        # Queue used for level order traversal (BFS)
        # Start with the root node
        q = collections.deque([root])

        # Continue until all levels are processed
        while q:

            # Will store the last node seen at current level
            rightSide = None

            # Number of nodes present in current level
            qLen = len(q)

            # Process all nodes of the current level
            for i in range(qLen):

                # Remove node from front of queue
                node = q.popleft()

                # Ignore None nodes
                if node:

                    # Keep updating rightSide
                    # Final updated node of the level
                    # becomes the visible right side node
                    rightSide = node

                    # Add children for next level traversal
                    q.append(node.left)
                    q.append(node.right)

            # After finishing one level,
            # append the last visible node
            if rightSide:
                res.append(rightSide.val)

        return res