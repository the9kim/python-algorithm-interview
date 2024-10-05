from unittest import TestCase

from Algorithm.kakao.t21 import P4_2_Taxi_Ride_Sharing_Fare


class Test(TestCase):
    def setUp(self):
        self.p4 = P4_2_Taxi_Ride_Sharing_Fare

    def test_solution(self):
        n = 6
        s = 4
        a = 6
        b = 2
        fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22],
                 [1, 6, 25]]
        expected = 82

        answer = self.p4.solution(n, s, a, b, fares)

        self.assertEqual(expected, answer)
