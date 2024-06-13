from unittest import TestCase

from Algorithm.kakao.t20.P2_1_Bracket_Transformation import P2_1_Bracket_Transformation


class TestP2_1_Bracket_Transformation(TestCase):

    def setUp(self):
        self.p2 = P2_1_Bracket_Transformation()
    def test_solution(self):
        p = "()))((()"
        expected = "()(())()"

        answer = self.p2.solution(p)

        self.assertEqual(expected, answer)


