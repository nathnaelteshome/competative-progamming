class OrderedStream:

    def __init__(self, n: int):
        self.arr = [0] * n
        self.left = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        id = idKey - 1
        self.arr[id] = value

        if id > self.left:
            return []

        while self.left < len(self.arr) and self.arr[self.left]:
            self.left += 1
        return self.arr[id: self.left]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)