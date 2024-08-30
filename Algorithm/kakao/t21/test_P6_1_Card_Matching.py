from unittest import TestCase

from Algorithm.kakao.t21.P6_1_Card_Matching import P6_1_Card_Matching


class TestP6_1_Card_Matching(TestCase):
    def setUp(self):
        self.p6 = P6_1_Card_Matching()
    def test_solution(self):
        board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
        r = 1
        c = 0
        expected = 14

        answer = self.p6.solution(board, r, c)

        self.assertEquals(expected, answer)
