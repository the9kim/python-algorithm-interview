from unittest import TestCase

from Algorithm.kakao.t20.P1_1_String_Compression import P1_1_String_Compression


class TestP1_1_String_Compression(TestCase):
    def setUp(self):
        self.p1 = P1_1_String_Compression()
    def test_solution(self):
        s = "aabbaccc"
        expected = 7

        answer = self.p1.solution(s)

        self.assertEqual(expected, answer)
