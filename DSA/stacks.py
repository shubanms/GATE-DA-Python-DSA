# Import deque to implement the stack
from collections import deque

# Create the stack object
class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value: int):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def print(self):
        print(self.stack)
        
    def __str__(self) -> str:
        string = ''
        for item in self.stack:
            string += str(item)+" | "
            
        return string

# Create a new object of stack type
stack = Stack()
stack.print()

# Push elements onto the stack
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

# Pop the top most element form the stack
stack.pop()

stack.print()

# Print the top of the stack
print(stack.top())

# Print the whole stack
print(stack)