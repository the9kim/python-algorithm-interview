from unittest import TestCase

from Algorithm.kakao.t22 import P3_2_Parking_Fee


class Test(TestCase):
    def setUp(self):
        self.p3 = P3_2_Parking_Fee

    def test_solution(self):
        fees = [180, 5000, 10, 600]
        records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                   "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
        expected = [14600, 34400, 5000]

        answer = self.p3.solution(fees, records)

        self.assertEqual(expected, answer)
