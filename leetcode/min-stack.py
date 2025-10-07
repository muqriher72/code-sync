class MinStack:

    def __init__(self):
        self.stack1 = [] # stack to keep track of all elements
        self.stack2 = [inf] # stack to keep track of min element at each level

    def push(self, val: int) -> None:
        self.stack1.append(val)
        self.stack2.append(min(val, self.stack2[-1]))

    def pop(self) -> None:
        self.stack1.pop()
        self.stack2.pop()

    def top(self) -> int:
        return self.stack1[-1]

    def getMin(self) -> int:
        return self.stack2[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()