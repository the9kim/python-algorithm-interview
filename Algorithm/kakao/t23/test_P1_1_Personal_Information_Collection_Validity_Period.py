from unittest import TestCase

from Algorithm.kakao.t23.P1_1_Personal_Information_Collection_Validity_Period import \
    P1_1_Personal_Information_Collection_Validity_Period


class TestP1_1_Personal_Information_Collection_Validity_Period(TestCase):
    def setUp(self):
        self.p1 = P1_1_Personal_Information_Collection_Validity_Period()
    def test_solution(self):
        today = "2022.05.19"
        terms = ["A 6", "B 12", "C 3"]
        privacies = ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]
        expected = [1, 3]

        answer = self.p1.solution(today, terms, privacies)

        self.assertEqual(expected, answer)
