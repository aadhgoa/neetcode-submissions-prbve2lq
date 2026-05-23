# Each node in Trie stores:
# 1. children -> next characters
# 2. endOfWord -> marks complete word ending
class TrieNode:

    def __init__(self):

        # Dictionary to store child nodes
        #
        # Example:
        # {
        #   'a': TrieNode(),
        #   'b': TrieNode()
        # }
        self.children = {}

        # True if a complete word ends here
        self.endOfWord = False


class PrefixTree:

    def __init__(self):

        # Root node is empty starting node
        self.root = TrieNode()

    # ---------------- INSERT ----------------
    #
    # Insert word character by character
    #
    # Example:
    # insert("cat")
    #
    # root
    #  └── c
    #       └── a
    #            └── t (endOfWord = True)
    #
    def insert(self, word: str) -> None:

        # Start traversal from root
        curr = self.root

        # Traverse each character
        for c in word:

            # If character path does not exist,
            # create a new TrieNode
            if c not in curr.children:
                curr.children[c] = TrieNode()

            # Move to next node
            curr = curr.children[c]

        # Mark end of complete word
        curr.endOfWord = True

    # ---------------- SEARCH ----------------
    #
    # Return True only if COMPLETE word exists
    #
    # search("app") should be False
    # if only "apple" exists
    #
    def search(self, word: str) -> bool:

        # Start from root
        curr = self.root

        # Traverse character by character
        for c in word:

            # If path missing,
            # word does not exist
            if c not in curr.children:
                return False

            # Move to next node
            curr = curr.children[c]

        # Word exists ONLY if endOfWord is True
        return curr.endOfWord

    # ---------------- STARTSWITH ----------------
    #
    # Return True if prefix path exists
    #
    # Example:
    # "app" should return True
    # if "apple" exists
    #
    def startsWith(self, prefix: str) -> bool:

        # Start from root
        curr = self.root

        # Traverse prefix characters
        for c in prefix:

            # Prefix path missing
            if c not in curr.children:
                return False

            # Move forward
            curr = curr.children[c]

        # Entire prefix exists
        return True