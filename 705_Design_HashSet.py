class MyHashSet:

    def __init__(self):
        self.size = 1000
        self.arr = [None]*self.size

    def hash1(self,key):
        return (key % self.size)

    def hash2(self,key):
        return (key // self.size)

    def add(self, key: int) -> None:
        main_idx = self.hash1(key)
        bucket_idx = self.hash2(key)
        if self.arr[main_idx] == None:
            if main_idx == 0:
                self.arr[main_idx] = [False]*(self.size + 1)
            else:
                self.arr[main_idx] = [False]*(self.size)
        self.arr[main_idx][self.hash2(key)] = True

    def remove(self, key: int) -> None:
        main_idx = self.hash1(key)
        bucket_idx = self.hash2(key)
        if self.arr[main_idx]:
            self.arr[main_idx][self.hash2(key)] = False
            return
        else:
            return

    def contains(self, key: int) -> bool:
        main_idx = self.hash1(key)
        bucket_idx = self.hash2(key)
        if self.arr[main_idx]:
            return (self.arr[main_idx][self.hash2(key)])
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)