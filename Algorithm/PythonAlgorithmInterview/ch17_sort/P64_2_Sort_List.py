from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class P64_1_Sort_List:

    def quick_sort(self, head: ListNode, tail: ListNode):
        if head == tail:
            return

        pivot = head
        left = head
        right = head.next

        while right != tail:
            if right.val < pivot.val:
                left = left.next
                left.val, right.val = right.val, left.val

            right = right.next

        pivot.val, left.val = left.val, pivot.val

        self.quick_sort(head, left)
        self.quick_sort(left.next, tail)

    def sortList(self, head:Optional[ListNode]) -> ListNode:
        self.quick_sort(head, None)
        return head





if __name__ == '__main__':
    node4 = ListNode(2)
    node3 = ListNode(4, node4)
    node2 = ListNode(1, node3)
    node1 = ListNode(3, node2)

    p64 = P64_1_Sort_List()
    sort_list = p64.sortList(node1)

    print(sort_list)
