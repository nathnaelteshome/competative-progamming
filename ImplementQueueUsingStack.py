class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x) -> None:
        while self.stack1:
            self.stack2.append(self.stack1.pop())

        self.stack1.append(x)

        while self.stack2:
            self.stack1.append(self.stack2.pop())

    def pop(self) -> int:
        return self.stack1.pop()

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[-1]
        else:
            return 0

    def empty(self) -> bool:
        return not self.stack1


# obj = MyQueue()
# obj.push(5)
# print(obj.stack1)
# param_2 = obj.pop()
# print("param_2", obj.stack1)
# param_3 = obj.peek()
# print("peeked", param_3)
# param_4 = obj.empty()
# print("isEmpty", param_4)
