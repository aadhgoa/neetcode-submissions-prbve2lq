# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    # ---------------- SERIALIZE ----------------
    # Convert tree -> string
    #
    # We use DFS preorder traversal:
    # Root -> Left -> Right
    #
    # Null nodes are stored as 'N'
    #
    # Example:
    #
    #       1
    #      / \
    #     2   3
    #
    # Serialized:
    # "1,2,N,N,3,N,N"
    #
    def serialize(self, root: Optional[TreeNode]) -> str:

        # Stores serialized values
        res = []

        def dfs(node):

            # If node is null,
            # store marker 'N'
            if not node:
                res.append('N')
                return

            # Store current node value
            res.append(str(node.val))

            # Serialize left subtree
            dfs(node.left)

            # Serialize right subtree
            dfs(node.right)

        dfs(root)

        # Convert list into single string
        return ','.join(res)

    # ---------------- DESERIALIZE ----------------
    # Convert string -> tree
    #
    # We rebuild tree using same preorder order:
    # Root -> Left -> Right
    #
    # 'N' means null node
    #
    def deserialize(self, data: str) -> Optional[TreeNode]:

        # Split serialized string into list
        vals = data.split(',')

        # Pointer to track current index in vals
        self.i = 0

        def dfs():

            # If current value is 'N',
            # this node is null
            if vals[self.i] == 'N':
                self.i += 1
                return None

            # Create current node
            node = TreeNode(int(vals[self.i]))

            # Move pointer forward
            self.i += 1

            # Build left subtree
            node.left = dfs()

            # Build right subtree
            node.right = dfs()

            return node

        return dfs()