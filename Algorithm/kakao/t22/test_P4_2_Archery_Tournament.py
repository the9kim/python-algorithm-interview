from unittest import TestCase

from Algorithm.kakao.t22 import P4_2_Archery_Tournament


class Test(TestCase):

    def setUp(self):
        self.p4 = P4_2_Archery_Tournament

    def test_solution(self):
        n = 5
        info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
        expected = [0, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0]

        answer = self.p4.solution(n, info)

        self.assertEqual(expected, answer)

    def test_solution2(self):
        n = 1
        info = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        expected = [-1]

        answer = self.p4.solution(n, info)

        self.assertEqual(expected, answer)
    def test_solution3(self):
        n = 9
        info = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
        expected = [1, 1, 2, 0, 1, 2, 2, 0, 0, 0, 0]

        answer = self.p4.solution(n, info)

        self.assertEqual(expected, answer)
