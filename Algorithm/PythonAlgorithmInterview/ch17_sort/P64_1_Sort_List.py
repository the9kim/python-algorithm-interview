class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class P64_1_Sort_List:
        def mergeLists(self, left: ListNode, right: ListNode) -> ListNode:
            if left and right:
                if left.val > right.val:
                    left, right = right, left

                left.next = self.mergeLists(left.next, right)

                return left

            return left or right

        def sortList(self, head: ListNode) -> ListNode:
            if not (head and head.next):
                return head

            # 1.
            slow = head
            fast = head
            half = None

            while fast is not None and fast.next is not None:
                half = slow
                slow = slow.next
                fast = fast.next.next

            half.next = None
            left = self.sortList(head)
            right = self.sortList(slow)

            # 2.
            return self.mergeLists(left, right)
