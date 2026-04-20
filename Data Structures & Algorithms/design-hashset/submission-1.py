class MyHashSet:

    def __init__(self):
        self.size = 10007
        self.table = [[] for _ in range(self.size)]
    def _hash(self, key:int) -> None:
        return key % self.size

    def add(self, key: int) -> None:
        bucket_id = self._hash(key)
        bucket = self.table[bucket_id]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        bucket_id = self._hash(key)

        bucket = self.table[bucket_id]

        if key in bucket:

            bucket.remove(key)

    def contains(self, key: int) -> bool:
        bucket_id = self._hash(key)
        bucket = self.table[bucket_id]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)