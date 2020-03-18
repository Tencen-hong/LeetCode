class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.itemsPerBuckect = 1001
        self.hashmap = [[] for _ in range(self.buckets)]

    def hash_(self, key):
        return key % self.buckets

    def pos(self, key):
        return key // self.buckets

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hashkey = self.hash_(key)
        if not self.hashmap[hashkey]:                 # 没有产生冲突，直接填入buckets中
            self.hashmap[hashkey] = [None] * self.itemsPerBuckect
        self.hashmap[hashkey][self.pos(key)] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hashkey = self.hash_(key)
        if(not self.hashmap[hashkey]) or self.hashmap[hashkey][self.pos(key)] == None:      # 没有找到这个值
            return -1
        else:
            return self.hashmap[hashkey][self.pos(key)]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hashkey = self.hash_(key)
        if self.hashmap[hashkey]:
            self.hashmap[hashkey][self.pos(key)] = None


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
