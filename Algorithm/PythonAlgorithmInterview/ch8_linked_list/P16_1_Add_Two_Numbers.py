from typing import Optional


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

class P16_1_Add_Two_Numbers:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        answer = ListNode(0)
        temp = answer

        carry = 0

        while l1 or l2 or carry == 1:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            remainder = (sum + carry) % 10
            carry = (sum + carry) // 10

            temp.next = ListNode(remainder)
            temp = temp.next

        return answer.next