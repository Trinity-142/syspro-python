class LRUCache:
    def __init__(self, capacity=16):
        self.capacity = capacity
        self.cache = {}

    def put(self, key, value):
        if key in self.cache:
            self.cache[key] = [value, self.cache[key][1]]
            return
        elif len(self.cache) == self.capacity:
            self.cache.pop(min(iter(self.cache), key=(lambda key: self.cache[key][1])))
        self.cache[key] = [value, 0]

    def get(self, key):
        if key in self.cache:
            self.cache[key][1] += 1
            return self.cache[key][0]
        return None


def test():
    lru = LRUCache(5)
    for i in range(lru.capacity):
        lru.put(i, i + 1)
        assert lru.get(i + 1) is None
        assert lru.get(i) == i + 1
        assert lru.cache == {x: [x + 1, 1] for x in range(i + 1)}

    lru.put(4, 6)
    assert lru.cache == {0: [1, 1], 1: [2, 1], 2: [3, 1], 3: [4, 1], 4: [6, 1]}
    lru.put(5, 7)
    assert lru.cache == {1: [2, 1], 2: [3, 1], 3: [4, 1], 4: [6, 1], 5: [7, 0]}
    lru.put(6, 8)
    assert lru.cache == {1: [2, 1], 2: [3, 1], 3: [4, 1], 4: [6, 1], 6: [8, 0]}


if __name__ == 'main':
    test()