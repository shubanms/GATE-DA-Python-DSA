from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self):
        self.stack = deque()

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def top(self):
        print(self.stack[-1])

    def print(self):
        print(self.stack)


class LinkedListStack:
    def __init__(self):
        self.root = None

    def push(self, value):
        node = Node(value)
        node.next = self.root
        self.root = node

    def pop(self):
        value = self.root.value
        self.root = self.root.next

        return value

    def top(self):
        pass

    def is_empty(self):
        pass

    def size(self):
        ptr = self.root

        size = 0

        while ptr:
            size += 1
            ptr = ptr.next

        return size

    def print(self):
        ptr = self.root

        while ptr:
            print(ptr.value)
            ptr = ptr.next


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.print()

print(stack.pop())

stack.print()

stack.top()

print("*"*30)

stack = LinkedListStack()

stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)

stack.print()

print(stack.pop())

stack.print()
