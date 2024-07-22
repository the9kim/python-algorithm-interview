from unittest import TestCase

from Algorithm.kakao.t19.P5_1_Path_Finding_Game import P5_1_Path_Finding_Game


class TestP5_1_Path_Finding_Game(TestCase):

    def setUp(self):
        self.p5 = P5_1_Path_Finding_Game()
    def test_solution(self):
        nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
        expected = [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

        answer = self.p5.solution(nodeinfo)

        self.assertEquals(expected, answer)
