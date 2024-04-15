from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch17_sort import P66_1_Insertion_Sort_List
from Algorithm.PythonAlgorithmInterview.ch17_sort.P66_1_Insertion_Sort_List import ListNode


class TestP66_1_Insertion_Sort_List(TestCase):
    def setUp(self) -> None:
        self.p66 = P66_1_Insertion_Sort_List

    def test_insertion_sort_list(self):
        node5 = ListNode(0)
        node4 = ListNode(4, node5)
        node3 = ListNode(3, node4)
        node2 = ListNode(5, node3)
        node1 = ListNode(-1, node2)

        answer = self.p66.P66_1_Insertion_Sort_List.insertionSortList(self, node1)

        print(answer.val)
        print(answer.next.val)
        print(answer.next.next.val)
        print(answer.next.next.next.val)
        print(answer.next.next.next.next.val)



