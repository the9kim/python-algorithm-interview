from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class P66_1_Insertion_Sort_List:
    def insertionSortList(self, head:Optional[ListNode]) -> Optional[ListNode]:
        parent = ListNode()
        p = parent

        while head:
            # 1. Remove an element from the input List
            head_next = head.next
            head.next = None

            # 2. Find the location it belongs within the sorted List
            while p.next and p.next.val < head.val:
                p = p.next

            p_next = p.next
            p.next = head
            head.next = p_next
            head = head_next

            if head and p.val > head.val:
                p = parent

        return parent.next








