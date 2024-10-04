from unittest import TestCase

from Algorithm.kakao.t21 import P3_2_Rank_Search


class Test(TestCase):
    def setUp(self):
        self.p3 = P3_2_Rank_Search
    def test_solution(self):
        info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
        query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

        expected = [1,1,1,1,2,4]

        answer = self.p3.solution(info, query)

        self.assertEqual(expected, answer)

