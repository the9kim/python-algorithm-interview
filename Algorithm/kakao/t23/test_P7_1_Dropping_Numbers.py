from unittest import TestCase

from Algorithm.kakao.t23.P7_1_Dropping_Numbers import P7_1_Dropping_Numbers


class TestP7_1_Dropping_Numbers(TestCase):
    def setUp(self):
        self.p7 = P7_1_Dropping_Numbers()
    def test_solution(self):
        edges = [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]]
        target = [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]
        expected = [1, 1, 2, 2, 2, 3, 3]

        answer = self.p7.solution(edges, target)

        self.assertEquals(expected, answer)