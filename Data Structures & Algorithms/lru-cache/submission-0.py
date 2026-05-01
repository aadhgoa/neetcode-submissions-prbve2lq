class Node:

    def __init__(self, key, val):

        self.key = key

        self.val = val

        self.prev = None

        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.left = Node(0, 0)   # LRU
        self.right = Node(0, 0)  # MRU

        self.left.next = self.right
        self.right.prev = self.left

         # remove node from list

    def remove(self, node):

        prev, nxt = node.prev, node.next

        prev.next = nxt

        nxt.prev = prev

    # insert node at MRU (right side)

    def insert(self, node):

        prev, nxt = self.right.prev, self.right

        prev.next = node

        node.prev = prev

        node.next = nxt

        nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            # move to MRU

            self.remove(node)

            self.insert(node)

            # Move to MRU 
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:

            self.remove(self.cache[key])

        node = Node(key, value)

        self.cache[key] = node

        self.insert(node)

        # remove LRU if needed

        if len(self.cache) > self.cap:

            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]

        
