class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None

class P13_1_Palindrome_Linked_List:
    def isPalindrome(self, head: ListNode) -> bool:

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        if fast is not None:
            slow = slow.next

        rev = None

        while slow:
            next = slow.next
            slow.next = rev
            rev = slow
            slow = next

        while rev:
            if head.val != rev.val:
                return False;
            head = head.next
            rev = rev.next

        return True

