from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache.keys():
            return -1
        val = self.cache[key]
        self.cache.move_to_end(key)

        return val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache.keys():
            if len(self.cache) >= self.capacity:
                _ = self.cache.popitem(last=False)

        self.cache[key] = value
        self.cache.move_to_end(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
