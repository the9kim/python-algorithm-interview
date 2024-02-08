class MyCircularQueue:

    # The solution the book suggests
    def __init__(self, k: int):
        self.q = [None] * k
        self.max_len = k
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.max_len
            return True

        return False

    def deQueue(self) -> bool:
        if self.q[self.front] is not None:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.max_len
            return True

        return False

    def Front(self) -> int:
        return -1 if self.q[self.front] is None else self.q[self.front]

    def Rear(self) -> int:
        return -1 if self.q[self.rear - 1] is None else self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        if self.front == self.rear and self.q[self.front] is None:
            return True
        return False

    def isFull(self) -> bool:
        if self.front == self.rear and self.q[self.front] is not None:
            return True
        return False

