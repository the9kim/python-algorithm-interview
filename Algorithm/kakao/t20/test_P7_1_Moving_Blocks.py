from unittest import TestCase

from Algorithm.kakao.t20.P7_1_Moving_Blocks import P7_1_Moving_Blocks


class TestP7_1_Moving_Blocks(TestCase):

    def setUp(self):
        self.p7 = P7_1_Moving_Blocks()

    def test_solution(self):
        board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
        expected = 7

        answer = self.p7.solution(board)

        self.assertEquals(expected, answer)