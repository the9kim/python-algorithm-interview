from unittest import TestCase

from Algorithm.kakao.t22.P7_1_Disappearing_Platform import P7_1_Disappearing_Platform


class TestP7_1_Disappearing_Platform(TestCase):
    def setUp(self):
        self.p7 = P7_1_Disappearing_Platform()
    def test_solution(self):
        board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
        aloc = [1, 0]
        bloc = [1, 2]
        expected = 5

        answer = self.p7.solution(board, aloc, bloc)

        self.assertEquals(expected, answer)
