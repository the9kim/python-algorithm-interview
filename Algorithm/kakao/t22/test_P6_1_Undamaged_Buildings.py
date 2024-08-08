from unittest import TestCase

from Algorithm.kakao.t22.P6_1_Undamaged_Buildings import P6_1_Undamaged_Building


class TestP6_1_Undamaged_Building(TestCase):

    def setUp(self):
        self.p6 = P6_1_Undamaged_Building()

    def test_solution(self):
        board = [[5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5], [5, 5, 5, 5, 5]]
        skill = [
            [1, 0, 0, 3, 4, 4],
            [1, 2, 0, 2, 3, 2],
            [2, 1, 0, 3, 1, 2],
            [1, 0, 1, 3, 3, 1]
        ]
        expected = 10

        answer = self.p6.solution(board, skill)

        self.assertEquals(expected, answer)
