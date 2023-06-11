class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map keys to nodes
        # dummy nodes for lru and mru
        # left = least, right = most
        self.left = self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    def detach(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def prepend(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.cache:
            self.detach(self.cache[key])
            self.prepend(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.detach(self.cache[key])
        self.cache[key] = Node(key, value)
        self.prepend(self.cache[key])
        if len(self.cache) > self.cap:
            # remove from linkedlist and deleted cache from dict
            lru = self.left.next
            self.detach(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
