from unittest import TestCase

from Algorithm.kakao.t20.P5_1_Pillars_and_Beams import P5_1_Pillars_and_Beams


class TestP5_1_Pillars_and_Beams(TestCase):
    def setUp(self):
        self.p5 = P5_1_Pillars_and_Beams()
    def test_solution(self):
        n = 5
        build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
        expected = [[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]]

        answer = self.p5.solution(n, build_frame)

        self.assertEqual(expected, answer)

    def test_solution2(self):
        n = 5
        build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
        expected = [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]


        answer = self.p5.solution(n, build_frame)

        self.assertEqual(expected, answer)
