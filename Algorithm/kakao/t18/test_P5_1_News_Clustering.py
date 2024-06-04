from unittest import TestCase

from Algorithm.kakao.t18.P5_1_News_Clustering import P5_1_News_Clustering


class TestP5_1_News_Clustering(TestCase):
    def setUp(self):
        self.p5 = P5_1_News_Clustering()
    def test_solution(self):
        str1 = "FRANCE"
        str2 = "french"
        expected = 16384

        answer = self.p5.solution(str1, str2)

        self.assertEqual(expected, answer)

