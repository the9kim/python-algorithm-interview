from unittest import TestCase

from Algorithm.kakao.t22.P2_1_Number_of_Prime_Numbers import P2_1_Number_of_Prime_Numbers


class TestP2_1_Number_of_Prime_Numbers(TestCase):
    def setUp(self):
        self.p2 = P2_1_Number_of_Prime_Numbers()
    def test_solution(self):
        n = 437674
        k = 3
        expected = 3

        answer = self.p2.solution(n, k)

        self.assertEqual(expected, answer)
