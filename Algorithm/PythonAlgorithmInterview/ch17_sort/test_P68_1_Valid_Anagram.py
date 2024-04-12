from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch17_sort.P68_1_Valid_Anagram import P68_1_Valid_Anagram

class TestP68_1_Valid_Anagram(TestCase):
    def setUp(self) -> None:
        self.test = P68_1_Valid_Anagram()

    def test_sort_str(self):
        # given
        s = "anagram"
        expected = "aaagmnr"

        # when
        answer = self.test.sort_str(s)

        # then
        self.assertEquals(answer, expected)

    def test_is_anagram(self):
        # given
        s = "anagram"
        t = "nagaram"
        expected = True

        # when
        answer = self.test.isAnagram(s, t)

        # then
        self.assertEquals(answer, expected)
