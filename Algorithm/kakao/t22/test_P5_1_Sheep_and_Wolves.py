from unittest import TestCase

from Algorithm.kakao.t22.P5_1_Sheep_and_Wolves import P5_1_Sheep_and_Wovles


class TestP5_1_Sheep_and_Wovles(TestCase):

    def setUp(self):
        self.p5 = P5_1_Sheep_and_Wovles()

    def test_solution(self):
        info = [0,0,1,1,1,0,1,0,1,0,1,1]
        edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

        expected = 5

        answer = self.p5.solution(info, edges)

        self.assertEqual(expected, answer)
