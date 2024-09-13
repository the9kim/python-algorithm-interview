from unittest import TestCase

from Algorithm.kakao.t20 import P1_2_String_Compression


class Test(TestCase):
    def setUp(self):
        self.p1 = P1_2_String_Compression

    def test_solution(self):
        s = "aabbaccc"
        expected = 7

        answer = self.p1.solution(s)

        self.assertEqual(expected, answer)
