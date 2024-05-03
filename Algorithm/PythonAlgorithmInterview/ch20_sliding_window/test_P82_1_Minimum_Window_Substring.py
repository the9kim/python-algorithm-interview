from unittest import TestCase

from Algorithm.PythonAlgorithmInterview.ch20_sliding_window.P82_1_Minimum_Window_Substring import \
    P82_1_Minimum_Window_Substring


class TestP82_1_Minimum_Window_Substring(TestCase):
    def setUp(self):
        self.p82 = P82_1_Minimum_Window_Substring()
    def test_min_window(self):
        # given
        s = "ADOBECODEBANC"
        t = "ABC"
        expected = "BANC"

        # when
        answer = self.p82.minWindow(s, t)

        # then
        self.assertEqual(expected, answer)

    def test_min_window2(self):
        # given
        s = "cabwefgewcwaefgcf"
        t = "cae"
        expected = "cwae"

        # when
        answer = self.p82.minWindow(s, t)

        # then
        self.assertEqual(expected, answer)

