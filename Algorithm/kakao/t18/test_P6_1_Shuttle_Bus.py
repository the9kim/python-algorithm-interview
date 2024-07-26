from unittest import TestCase

from Algorithm.kakao.t18.P6_1_Shuttle_Bus import P6_1_Shuttle_Bus


class TestP6_1_Shuttle_Bus(TestCase):
    def setUp(self):
        self.p6 = P6_1_Shuttle_Bus()
    def test_solution(self):
        n = 2
        t = 10
        m = 2
        timetable = ["09:10", "09:09", "08:00"]
        expected = "09:09"

        answer = self.p6.solution(n, t, m, timetable)

        self.assertEquals(expected, answer)
