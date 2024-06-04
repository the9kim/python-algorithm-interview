from unittest import TestCase

from Algorithm.kakao.t19.P1_1_Failure_Rate import P1_1_Failure_Rate


class TestP1_1_Failure_Rate(TestCase):
    def setUp(self):
        self.p1 = P1_1_Failure_Rate()
    def test_solution(self):
        N = 5
        stages = [2, 1, 2, 6, 2, 4, 3, 3]
        expected = [3,4,2,1,5]

        answer = self.p1.solution(N, stages)

        self.assertEqual(expected, answer)
