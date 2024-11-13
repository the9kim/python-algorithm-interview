from unittest import TestCase

from Algorithm.kakao.t23 import P4_2_Representable_Binary_Tree


class Test(TestCase):
    def setUp(self):
        self.p4 = P4_2_Representable_Binary_Tree
    def test_solution(self):
        numbers = [7, 42, 5]
        expected = [1, 1, 0]

        answer = self.p4.solution(numbers)
        self.assertEqual(expected, answer)
