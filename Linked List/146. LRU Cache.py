class LRUCache:
    def __init__(self, capacity: int):
        # Double linked list with capacity
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        # Get key and update cache if exists
        if key in self.cache:
            # Update to first in cache
            self.cache.move_to_end(key, last=False)
            return self.cache[key]
        # Key not found
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)

        elif self.capacity:
            self.capacity -= 1
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)
            return
        else:
            self.cache.popitem(last=True)
            self.cache[key] = value
            self.cache.move_to_end(key, last=False)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
