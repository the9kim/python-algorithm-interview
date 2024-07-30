from unittest import TestCase

from Algorithm.kakao.t20.P6_2_Exteral_Wall_Inpection import P6_2_Exteral_Wall_Inspection


class TestP6_2_Exteral_Wall_Inspection(TestCase):

    def setUp(self):
        self.p6 = P6_2_Exteral_Wall_Inspection()

    def test_solution(self):
        n = 12
        weak =[1, 5, 6, 10]
        dist = [1, 2, 3, 4]

        expected = 2

        answer = self.p6.solution(n, weak, dist)

        self.assertEquals(expected, answer)
