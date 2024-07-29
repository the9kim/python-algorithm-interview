from unittest import TestCase

from Algorithm.kakao.t19.P7_1_Block_Game import P7_1_Block_Game


class TestP7_1_Block_Game(TestCase):
    def setUp(self):
        self.p7 = P7_1_Block_Game()
    def test_solution(self):
        board = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,4,0,0,0],[0,0,0,0,0,4,4,0,0,0],[0,0,0,0,3,0,4,0,0,0],[0,0,0,2,3,0,0,0,5,5],[1,2,2,2,3,3,0,0,0,5],[1,1,1,0,0,0,0,0,0,5]]
        expected = 2

        answer = self.p7.solution(board)

        self.assertEquals(expected, answer)
