from unittest import TestCase

from Algorithm.kakao.t21.P2_1_Menu_Renewal import P2_1_Menu_Renewal


class TestP2_1_Menu_Renewal(TestCase):

    def setUp(self):
        self.p2 = P2_1_Menu_Renewal()
    def test_solution(self):
        orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
        course = [2,3,4]
        expected = ["AC", "ACDE", "BCFG", "CDE"]

        answer = self.p2.solution(orders, course)

        self.assertEqual(expected, answer)
