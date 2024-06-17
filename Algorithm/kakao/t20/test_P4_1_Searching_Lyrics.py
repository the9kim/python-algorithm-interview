from unittest import TestCase

from Algorithm.kakao.t20.P4_1_Searching_Lyrics import P4_1_Searching_Lyrics


class TestP4_1_Searching_Lyrics(TestCase):

    def setUp(self):
        self.p4 = P4_1_Searching_Lyrics()
    def test_solution(self):
        words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
        queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

        expected = [3, 2, 4, 1, 0]

        answer = self.p4.solution(words, queries)

        self.assertEqual(expected, answer)


