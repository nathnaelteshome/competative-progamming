class MinStack:

    def __init__(self):
        self.stack1 = []

    def push(self, val: int) -> None:
        self.stack1.append(val)

    def pop(self) -> None:
        self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return min(self.stack1)

# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.stack1)
# print(obj.stack2)

# param_1 = obj.getMin()
# print("param_1", param_1)
# obj.pop()
# param_3 = obj.top()
# print("param_3", param_3)
# param_4 = obj.getMin()
# print("param_4", param_4)
