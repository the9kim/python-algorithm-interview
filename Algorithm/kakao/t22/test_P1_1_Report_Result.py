from unittest import TestCase

from Algorithm.kakao.t22.P1_1_Report_Result import P1_1_Report_Result


class TestP1_1_Report_Result(TestCase):

    def setUp(self):
        self.p1 = P1_1_Report_Result()
    def test_solution(self):
        id_list = ["muzi", "frodo", "apeach", "neo"]
        report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
        k = 2
        expected = [2,1,1,0]

        answer = self.p1.solution(id_list, report, k)

        self.assertEqual(expected, answer)


