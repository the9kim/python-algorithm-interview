class ListNode:
    def __init__(self):
        self.value = None
        self.next = None

class P15_Reverse_Linked_List:

    def reverseList(self, head: ListNode) -> ListNode:

        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev

            next, node.next = node.next, prev

            return reverse(next, node)
        return reverse(head)


