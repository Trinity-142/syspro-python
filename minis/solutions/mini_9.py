from collections import deque


class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = {}
        self.order = deque()

    def put(self, key, value):
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.popleft()
            self.cache.pop(oldest)

        self.cache[key] = value
        self.order.append(key)

    def get(self, key):
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return None


def test():
    lru = LRUCache(5)
    for i in range(lru.capacity):
        lru.put(i, i + 1)
        assert lru.get(i + 1) is None
        assert lru.get(i) == i + 1
        assert lru.cache == {x: x+1 for x in range(i + 1)}
        a = lru.order

    lru.put(4, 6)
    assert lru.cache == {0: 1, 1: 2, 2: 3, 3: 4, 4: 6}
    assert list(lru.order) == list(lru.cache.keys())
    lru.put(5, 7)
    assert lru.cache == {1: 2, 2: 3, 3: 4, 4: 6, 5: 7}
    assert list(lru.order) == list(lru.cache.keys())
    lru.put(6, 8)
    assert lru.cache == {2: 3, 3: 4, 4: 6, 5: 7, 6: 8}
    assert list(lru.order) == list(lru.cache.keys())


if __name__ == 'main':
    test()