class TrieNode:
    def __init__(self) -> None:

        # Maps character -> next TrieNode
        self.children = {}

        # True if a complete word ends here
        self.word = False


class WordDictionary:

    def __init__(self):

        # Root of Trie
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Insert a word into the Trie.

        Example:
        addWord("bad")

        root
          |
          b
          |
          a
          |
          d (word=True)
        """

        current_node = self.root

        for character in word:

            # Create node if path doesn't exist
            if character not in current_node.children:
                current_node.children[character] = TrieNode()

            # Move to next node
            current_node = current_node.children[character]

        # Mark end of complete word
        current_node.word = True

    def search(self, word: str) -> bool:
        """
        Supports:
        - Normal characters
        - '.' wildcard

        '.' can match any single character

        Example:

        Trie contains:
            bad
            dad
            mad

        search(".ad") -> True
        """

        def dfs(index, node):

            # Start traversal from current node
            current_node = node

            # Process remaining characters
            for i in range(index, len(word)):

                character = word[i]

                # Wildcard case
                #
                # '.' can match ANY character
                if character == ".":

                    # Try every possible child
                    for child_node in current_node.children.values():

                        # If any path succeeds,
                        # word exists
                        if dfs(i + 1, child_node):
                            return True

                    # No matching path found
                    return False

                # Normal character case
                else:

                    # Character path doesn't exist
                    if character not in current_node.children:
                        return False

                    # Move deeper in Trie
                    current_node = current_node.children[character]

            # Word exists only if
            # current node marks end of word
            return current_node.word

        return dfs(0, self.root)