from unittest import TestCase

from Algorithm.kakao.t21.P7_1_Minimizing_Sales_Decline import P7_1_Minimizaing_Sales_Decline


class TestP7_1_Minimizaing_Sales_Decline(TestCase):
    def setUp(self):
        self.p7 = P7_1_Minimizaing_Sales_Decline()
    def test_solution(self):
        sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
        links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
        expected = 44

        answer = self.p7.solution(sales, links)

        self.assertEquals(answer, expected)
