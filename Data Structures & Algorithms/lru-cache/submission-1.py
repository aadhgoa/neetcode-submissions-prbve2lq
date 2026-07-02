class Node:
    """
    Doubly Linked List Node

    Stores:
    - key   (needed when removing from hash map)
    - value (actual cached value)
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.previous = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        """
        Data Structures

        1. HashMap
           Key -> Node

           Provides O(1) lookup.

        2. Doubly Linked List

           Maintains usage order.

           Left  -> Least Recently Used (LRU)

           Right -> Most Recently Used (MRU)
        """

        self.capacity = capacity

        # key -> Node
        self.cache = {}

        # Dummy nodes simplify insertion/removal
        self.least_recent = Node(0, 0)
        self.most_recent = Node(0, 0)

        self.least_recent.next = self.most_recent
        self.most_recent.previous = self.least_recent

    # ----------------------------------------
    # Remove a node from the linked list
    # ----------------------------------------
    def remove_node(self, node):

        previous_node = node.previous
        next_node = node.next

        previous_node.next = next_node
        next_node.previous = previous_node

    # ----------------------------------------
    # Insert node just before MRU dummy
    #
    # Newly accessed node becomes
    # the Most Recently Used.
    # ----------------------------------------
    def insert_at_most_recent(self, node):

        previous_node = self.most_recent.previous

        previous_node.next = node
        node.previous = previous_node

        node.next = self.most_recent
        self.most_recent.previous = node

    def get(self, key: int) -> int:
        """
        If key exists:

        Move node to MRU position
        because it was just used.
        """

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Remove from current position
        self.remove_node(node)

        # Insert at MRU position
        self.insert_at_most_recent(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update a cache entry.
        """

        # Existing key
        if key in self.cache:

            existing_node = self.cache[key]

            self.remove_node(existing_node)

            del self.cache[key]

        new_node = Node(key, value)

        self.cache[key] = new_node

        self.insert_at_most_recent(new_node)

        # Cache exceeded capacity
        if len(self.cache) > self.capacity:

            # First real node after dummy
            # is the Least Recently Used.
            least_recently_used = self.least_recent.next

            self.remove_node(
                least_recently_used
            )

            del self.cache[
                least_recently_used.key
            ]