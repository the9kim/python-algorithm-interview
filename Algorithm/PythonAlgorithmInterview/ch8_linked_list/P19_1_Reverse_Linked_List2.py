from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class P19_1_Reverse_Linked_List2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        root = ListNode()
        root.next = head

        start = root

        for i in range(left - 1):
            start = start.next

        end = start.next
        for i in range(right - left):
            temp = start.next
            start.next = end.next
            end.next = end.next.next
            start.next.next = temp

        return root.next