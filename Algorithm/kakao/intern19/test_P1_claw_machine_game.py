from unittest import TestCase

from Algorithm.kakao.intern19.P1_claw_machine_game import P1_claw_machine_game


class TestP1_claw_machine_game(TestCase):
    def setUp(self):
        self.p1 = P1_claw_machine_game()

    def test_solution(self):
        board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
        moves = [1,5,3,5,1,2,1,4]
        expected = 4

        answer = self.p1.solution(board, moves)

        self.assertEquals(expected, answer)