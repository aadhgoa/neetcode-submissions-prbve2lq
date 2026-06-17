class TrieNode:
    def __init__(self):

        # Character -> Next Trie Node
        self.children = {}

        # Marks end of a complete word
        self.is_word = False

    def add_word(self, word_to_insert):

        current_trie_node = self

        for character in word_to_insert:

            if character not in current_trie_node.children:
                current_trie_node.children[character] = TrieNode()

            current_trie_node = (
                current_trie_node.children[character]
            )

        current_trie_node.is_word = True


class Solution:
    def findWords(
        self,
        board: List[List[str]],
        words: List[str]
    ) -> List[str]:

        # ----------------------------------
        # Build Trie
        # ----------------------------------

        trie_root = TrieNode()

        for word in words:
            trie_root.add_word(word)

        total_rows = len(board)
        total_cols = len(board[0])

        # Stores all discovered words
        found_words = set()

        # Cells used in current DFS path
        visited_cells = set()

        def dfs(
            row,
            col,
            current_trie_node,
            current_word
        ):
            """
            Traverse board and Trie together.

            Board Path:
                o -> a -> t

            Trie Path:
                root -> o -> a -> t

            If board path is not present
            in Trie, stop immediately.
            """

            # ------------------------------
            # Invalid Conditions
            # ------------------------------

            if (
                row < 0
                or col < 0
                or row >= total_rows
                or col >= total_cols
                or (row, col) in visited_cells
            ):
                return

            current_character = board[row][col]

            # Current board character
            # does not continue any Trie path
            if (
                current_character
                not in current_trie_node.children
            ):
                return

            # ------------------------------
            # Choose
            # ------------------------------

            visited_cells.add((row, col))

            current_trie_node = (
                current_trie_node.children[
                    current_character
                ]
            )

            current_word += current_character

            # ------------------------------
            # Found complete word
            # ------------------------------

            if current_trie_node.is_word:
                found_words.add(current_word)

            # ------------------------------
            # Explore Neighbors
            # ------------------------------

            dfs(
                row + 1,
                col,
                current_trie_node,
                current_word
            )

            dfs(
                row - 1,
                col,
                current_trie_node,
                current_word
            )

            dfs(
                row,
                col + 1,
                current_trie_node,
                current_word
            )

            dfs(
                row,
                col - 1,
                current_trie_node,
                current_word
            )

            # ------------------------------
            # Backtrack
            # ------------------------------

            visited_cells.remove((row, col))

        # ----------------------------------
        # Start DFS from every cell
        # ----------------------------------

        for row in range(total_rows):
            for col in range(total_cols):

                dfs(
                    row,
                    col,
                    trie_root,
                    ""
                )

        return list(found_words)