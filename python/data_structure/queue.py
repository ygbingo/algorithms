"""
队列: 其实python里有自己的queue和dequeue
"""


class Queue:
    def __init__(self):
        self.Queue = []

    def enqueue(self, x):
        self.Queue.append(x)

    def dequeue(self):
        return self.Queue.pop(0)