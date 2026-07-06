class MinStack:

    def __init__(self):
        self.stack = []
        self.minS = [] # keep track of the min at that point of the stack

    def push(self, val: int) -> None:
        self.stack.append(val)
    
        # Compare the last pushed elemenet in minS
        if len(self.minS) == 0 or self.minS[-1] > val:
            self.minS.append(val)
        else:
            self.minS.append(self.minS[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.minS.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minS[-1]
        