import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class P27_1_Merge_k_Sorted_Lists:
    def mergekLists(self, lists: list[ListNode]) -> list[ListNode]:

        head = ListNode()
        tail = head

        heap = []

        # Add heads on the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i, lists[i]))



        while heap:
            node = heapq.heappop(heap)
            tail.next = node[2]
            tail = tail.next
            if tail.next:
                heapq.heappush(heap, (tail.next.val, node[1], tail.next))

        return head.next

