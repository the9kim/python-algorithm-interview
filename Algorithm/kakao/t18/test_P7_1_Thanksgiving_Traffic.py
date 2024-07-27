from unittest import TestCase

from Algorithm.kakao.t18.P7_1_Thanksgiving_Traffic import P7_1_Thankgiving_Traffic


class TestP7_1_Thankgiving_Traffic(TestCase):
    def setUp(self):
        self.p7 = P7_1_Thankgiving_Traffic()

    def test_solution(self):
        lines = [
            "2016-09-15 01:00:04.001 2.0s",
            "2016-09-15 01:00:07.000 2s"
        ]
        expected = 1

        answer = self.p7.solution(lines)

        self.assertEquals(expected, answer)

    def test_solution2(self):
        lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

        expected = 2

        answer = self.p7.solution(lines)

        self.assertEquals(expected, answer)
