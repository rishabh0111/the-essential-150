'''
https://leetcode.com/problems/min-stack
'''

# 1> Brute Force
'''
Time complexity: O(n) for getMin() and O(1) for other operations.
Space complexity: O(n) for getMin() and O(1) for other operations.
'''
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.stack[-1]

        while len(self.stack):
            mini = min(mini, self.stack[-1])
            tmp.append(self.stack.pop())

        while len(tmp):
            self.stack.append(tmp.pop())

        return mini
        
# 2> Two Stacks
'''
Time complexity: O(1) for all operations.
Space complexity: O(n)
'''
class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        value = min(value, self.minStack[-1] if self.minStack else value)
        self.minStack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
# 3> One Stack
'''
Time complexity: O(1) for all operations.
Space complexity: O(n)
'''
class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []

    def push(self, value: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = value
        else:
            self.stack.append(value - self.min)
            if value < self.min:
                self.min = value

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()
        if pop < 0:
            self.min = self.min - pop

    def top(self) -> int:
        top = self.stack[-1]

        if top > 0:
            return top + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min