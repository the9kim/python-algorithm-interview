from unittest import TestCase

from Algorithm.kakao.t20 import P3_2_Lock_and_Key


class Test(TestCase):
    def setUp(self):
        self.p3 = P3_2_Lock_and_Key

    def test_solution(self):
        key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
        lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
        expected = True

        answer = self.p3.solution(key, lock)

        self.assertEqual(expected, answer)
