class MinStack:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, val: int) -> None:
        self.stack1.append(val)
        if not self.stack2:
            self.stack2.append([val, 1])

        else:
            if not self.stack2 or val < self.stack2[-1][0]:
                self.stack2.append([val, 1])
            elif self.stack2[-1][0] == val:
                self.stack2[-1][1] += 1

    def pop(self) -> None:
        if self.stack2[-1][0] == self.stack1[-1]:
            self.stack2[-1][1] -= 1
        if self.stack2[-1][1] == 0:
            self.stack2.pop()

        return self.stack1.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1][0]


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
