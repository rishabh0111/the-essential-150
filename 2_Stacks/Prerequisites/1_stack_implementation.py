class Stack:
    def __init__(self):
        # Underlying storage
        self.items = []

    def push(self, value):
        # Add elements to top
        self.items.append(value)

    def pop(self):
        # Prevenet invalid removal
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        # Remove top element
        return self.items.pop()
        
    def peek(self):
        # Prevent invalid read
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        # Return top element
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
s = Stack()

s.push(1)
s.push(2)
s.push(3)

print(s.peek())   # 3
print(s.pop())    # 3
print(s.pop())    # 2
print(s.size())   # 1