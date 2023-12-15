"""
栈
"""


class Stack:
    def __init__(self):
        self.Stack = []

    def is_empty(self):
        if len(self.Stack) == 0:
            return True
        return False

    def push(self, x):
        self.Stack.append(x)

    def pop(self):
        return self.Stack.pop()