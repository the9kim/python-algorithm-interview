from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch20_sliding_window.P83_1_Longest_Repeating_Character_Replacement import \
    P83_1_Longest_Repeating_Character_Replacement


class TestP83_1_Longest_Repeating_Character_Replacement(TestCase):

    def setUp(self):
        self.p83 = P83_1_Longest_Repeating_Character_Replacement()
    def test_character_replacement(self):
        # given
        s = "AABABBA"
        k = 1
        expected = 4

        # when
        answer = self.p83.characterReplacement(s, k)

        # then
        self.assertEqual(expected, answer)
