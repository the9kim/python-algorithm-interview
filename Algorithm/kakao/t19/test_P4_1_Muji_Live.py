from unittest import TestCase

from Algorithm.kakao.t19.P4_1_Muji_Live import P4_1_Muji_Live


class TestP4_1_Muji_Live(TestCase):
    def setUp(self):
        self.p4 = P4_1_Muji_Live()

    def test_solution(self):
        food_times = [3, 1, 2]
        k = 5
        expected = 1

        answer = self.p4.solution(food_times, k)

        self.assertEquals(expected, answer)
