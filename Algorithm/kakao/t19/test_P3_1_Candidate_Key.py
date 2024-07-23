from unittest import TestCase

from Algorithm.kakao.t19.P3_1_Candidate_Key import P3_1_Candidate_Key


class TestP3_1_Candidate_Key(TestCase):
    def setUp(self):
        self.p3 = P3_1_Candidate_Key()

    def test_solution(self):
        relation = [["100", "ryan", "music", "2"], ["200", "apeach", "math", "2"], ["300", "tube", "computer", "3"],
                    ["400", "con", "computer", "4"], ["500", "muzi", "music", "3"], ["600", "apeach", "music", "2"]]
        expected = 2

        answer = self.p3.solution(relation)
        self.assertEquals(expected, answer)
