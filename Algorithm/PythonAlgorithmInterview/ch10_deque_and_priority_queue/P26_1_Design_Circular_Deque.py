class MyCircularDeque:

    def __init__(self, k: int):
        self.len = 0
        self.size = k
        self.head = self.DoublyLinkedList(0)
        self.tail = self.DoublyLinkedList(0)

        # Initialize connection of the head and the tail
        self.head.right = self.tail
        self.tail.left = self.head

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            node = self.DoublyLinkedList(value)
            node.left = self.head
            node.right = self.head.right

            self.head.right.left = node
            self.head.right = node

            self.len += 1

            return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        else:
            node = self.DoublyLinkedList(value)

            node.left = self.tail.left
            node.right = self.tail

            self.tail.left.right = node
            self.tail.left = node

            self.len += 1
            return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.head.right.right.left = self.head
            self.head.right = self.head.right.right

            self.len -= 1
            return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        else:
            self.tail.left.left.right = self.tail
            self.tail.left = self.tail.left.left

            self.len -= 1

            return True

    def getFront(self) -> int:
        return -1 if self.isEmpty() else self.head.right.value

    def getRear(self) -> int:
        return -1 if self.isEmpty() else self.tail.left.value

    def isFull(self) -> bool:
        return self.len == self.size

    def isEmpty(self) -> bool:
        return self.len == 0

    class DoublyLinkedList:
        def __init__(self, value: int):
            self.left = None
            self.right = None
            self.value = value
